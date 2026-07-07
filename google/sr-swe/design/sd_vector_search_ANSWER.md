# System Design: Vector Search / Semantic Search Service — ANSWER

---

## Clarifications to establish upfront

- 1 billion 768-dim vectors (e.g. document embeddings)
- Approximate nearest neighbor (ANN) acceptable — exact KNN too slow at this scale
- < 50ms P99 query latency, 10K QPS
- Upserts visible within 1 minute (near-real-time)
- Metadata filtering required (e.g. filter by category, date, tenant)

---

## High-Level Architecture

```
Client
  │
  ▼
Query Service  ←── Embedding Model (converts text → vector at query time)
  │
  ▼
ANN Index Cluster (sharded)
  ├── Shard 0: vectors 0..200M   (HNSW or IVF index in memory)
  ├── Shard 1: vectors 200M..400M
  ├── ...
  └── Shard 4: vectors 800M..1B
  │
  ▼ (merge top-K from each shard)
Result Merger → return top-K globally
  │
  ▼
Metadata Store (Spanner/Bigtable) ── apply filters, enrich results
```

---

## Why Not Exact KNN at Scale?

Exact KNN requires comparing the query against every vector: O(N × D) per query.
For 1B vectors × 768 dims × 10K QPS = **7.68 × 10^15 operations/second** — not feasible.

ANN trades a small recall drop (e.g. 95% recall@10) for orders-of-magnitude speedup.
In practice, 95% recall is acceptable — missing 5% of relevant results is fine for
most search/recommendation use cases.

**Interview talking point**: "Exact KNN is O(N) per query. At 1B vectors and 10K QPS, that's ~10^13 dot products per second. ANN gets this down to O(log N) or O(sqrt(N)) by pre-building an index structure that prunes the search space."

---

## Indexing Algorithm

Two main choices:

**HNSW (Hierarchical Navigable Small World)** — preferred for low-latency online serving
- Graph-based: each vector is a node; edges connect nearby vectors
- Multi-layer graph: upper layers are coarse (few nodes), lower layers are dense
- Query: start at top layer, greedily navigate toward query vector, descend to finer layers
- Pros: very fast queries (O(log N)), high recall, incremental updates
- Cons: high memory (graph structure overhead), slow index build for billions of vectors

**IVF (Inverted File Index)** — preferred for massive corpora, batch workloads
- Cluster vectors into K centroids (K-means); each vector assigned to nearest centroid
- Query: find nearest centroids (nprobe of them), search only those clusters
- Add PQ (Product Quantization) for compression: IVF-PQ reduces memory 8-32x
- Pros: lower memory than HNSW, scales to billions
- Cons: slightly lower recall, less friendly to real-time updates

**Choice**: HNSW for < 100M vectors with latency priority; IVF-PQ for billion-scale with memory constraints. **Vertex AI Vector Search uses a custom ScaNN algorithm** (similar to IVF-PQ with optimized distance computation).

---

## Query Path

1. Client sends query text (or pre-computed vector)
2. Query Service calls embedding model if text → get 768-dim query vector
3. Query broadcast to all N shards in parallel
4. Each shard runs ANN search locally → returns local top-K with distances
5. Result Merger does a K-way merge across shard results → global top-K
6. Metadata Store lookup: fetch metadata for top-K IDs, apply any filters
7. Return ranked results with scores and metadata to client

**Total latency budget** (50ms P99):
- Embedding: ~10ms (if needed)
- Shard search (parallel): ~25ms
- Merge + metadata: ~5ms
- Network: ~5ms

---

## Index Updates (Real-Time Upserts)

**Challenge**: rebuilding a billion-vector index takes hours. Can't rebuild on every upsert.

**Solution: delta index + periodic merge**

1. **Write path**: new/updated vectors go to a small in-memory **delta index** (HNSW, fast to update)
2. **Query path**: search both the main index AND delta index, merge results
3. **Background merge**: periodically (every few minutes), merge delta into main index
4. **Delete**: mark vectors as deleted in a tombstone set; filter from results at query time; purged during merge

This is the same pattern as LSM trees (used in Bigtable/RocksDB): fast writes to a small mutable structure, periodic compaction into a large immutable one.

---

## Metadata Filtering

**Challenge**: pure ANN returns nearest vectors by embedding similarity, ignoring metadata.
Filtering after ANN (post-filtering) is simple but breaks recall — if only 1% of vectors
match the filter, ANN might return 0 matching results in top-K.

**Approaches**:

1. **Post-filtering** (simple): run ANN → get top-10K → apply filter → return top-K
   - Works when filter selectivity is high (many matches)
   - Fails for rare categories (< 1% match)

2. **Pre-filtering** (accurate but slow): apply filter first → search only matching vectors
   - Build per-category sub-indexes
   - Expensive to maintain many sub-indexes

3. **Hybrid** (Vertex AI Vector Search approach): use filter to narrow candidate set,
   then run ANN on candidates
   - Store metadata alongside vectors; use bitmap indexes for filter attributes
   - At query time: compute filter bitmap, intersect with ANN graph traversal

---

## Scaling & Sharding

**Horizontal sharding**: partition vectors by ID range or hash
- Each shard holds ~200M vectors (~600GB at 768-dim float32)
- Query fan-out: all shards searched in parallel
- Replication: 3 replicas per shard for availability

**Hot shard mitigation**: consistent hashing or random assignment prevents hot spots

**Read scaling**: replicate popular shards; route read traffic across replicas

**Vertex AI Vector Search**: manages sharding automatically; exposes a single endpoint

---

## Tradeoffs

| Decision | Tradeoff |
|---|---|
| HNSW vs IVF-PQ | HNSW: lower latency, more memory; IVF-PQ: less memory, slightly lower recall |
| Post-filter vs pre-filter | Post: simple, fails low-selectivity; Pre: accurate, expensive index maintenance |
| Shard count | More shards → better parallelism, but more fan-out network overhead |
| Delta index size | Larger delta → fresher, but slower queries (more to search) |
| Recall vs. latency | Higher nprobe/ef_search → better recall, slower queries |

---

## Vertex AI Angle

- **Vertex AI Vector Search** (formerly Matching Engine) is exactly this system
- ScaNN (Scalable Nearest Neighbors) is Google's ANN algorithm — open-sourced, powers Matching Engine
- Supports streaming updates (upserts visible in ~1 min) and batch updates
- Integrates with Vertex AI embeddings API + RAG Engine for end-to-end RAG pipelines
- **RAG use case**: embed documents → store in Vector Search → at query time, embed user question → retrieve top-K chunks → pass to LLM as context

---

## Follow-up questions

1. "How do you evaluate recall?" → offline benchmark: compare ANN results to exact KNN on held-out queries; measure recall@K
2. "How would you support multi-tenancy?" → namespace per tenant with isolated indexes; shared infrastructure with quota per namespace
3. "How does this fit into a RAG pipeline?" → Vector Search is the retrieval layer; LLM is the generation layer; the key is embedding model consistency (same model for indexing and querying)
4. "What if the embedding model changes?" → re-embed and re-index the entire corpus; run both old and new indexes in parallel during migration (shadow traffic)
