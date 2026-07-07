# System Design: Vector Search / Semantic Search Service

**Difficulty**: Hard
**Relevance**: Vertex AI Vector Search (formerly Matching Engine), RAG pipelines, recommendation systems

---

## Problem Statement

Design a vector search service that, given a query embedding, returns the top-K
most similar vectors from a large corpus. This is the core building block for
semantic search, RAG (retrieval-augmented generation), and recommendation systems.

---

## Requirements to clarify (ask before designing)

- Corpus size? (millions vs. billions of vectors)
- Vector dimension? (768 for BERT, 1536 for OpenAI ada-002, 3072 for large models)
- Latency target? (< 50ms? < 10ms?)
- Freshness? (real-time index updates vs. batch rebuilds)
- Approximate or exact nearest neighbor? (ANN vs. exact KNN)
- Read/write ratio? (mostly reads with occasional bulk updates?)

---

## Functional Requirements

- Upsert vectors (add or update a vector by ID)
- Delete vectors by ID
- Query: given a query vector, return top-K nearest neighbors with scores
- Filter: optionally filter by metadata (e.g. `category=sports`)
- Namespaces: isolate different corpora (e.g. per-customer indexes)

## Non-Functional Requirements

- Corpus: 1 billion 768-dim vectors
- Query latency: < 50ms P99
- QPS: 10,000 queries/sec
- Index freshness: upserts visible within 1 minute
- 99.9% availability

---

## Your Design

### 1. High-Level Architecture

### 2. Why not exact KNN at scale?
(why ANN, and what's the tradeoff?)

### 3. Indexing Algorithm
(what algorithm? HNSW? IVF? why?)

### 4. Query Path
(step by step from query vector to top-K results)

### 5. Index Updates
(how do you handle real-time upserts to a billion-vector index?)

### 6. Metadata Filtering
(how do you combine vector similarity with attribute filters?)

### 7. Scaling & Sharding

### 8. Tradeoffs

---

## Mock Interview Notes (2026-07-06)

### What I got right
- Clarifying questions: corpus size, access patterns (read/write), SLA, who owns the vector DB
- Correctly identified why regular databases fail: semantic search needs embedding similarity, not exact match
- Right high-level architecture: API gateway → auth → write/query service separation → sharded fleet
- Hybrid search (BM25 + vector) knowledge showed real production experience
- Incremental indexing instinct for upserts was correct direction

### What to sharpen — detailed

---

#### 1. Exact KNN vs ANN — the fundamental tradeoff
**What exact KNN is**: compare query vector against every vector in corpus. O(N × D) per query.

**Why it fails at scale**:
```
1B vectors × 768 dims × 10K QPS = 7.68 × 10^15 ops/second — not feasible
```

**ANN (Approximate Nearest Neighbor)**: pre-builds an index structure that prunes the search space. Finds ~95% of true top-K results at O(log N) instead of O(N). The 5% recall loss is acceptable for search/recommendation.

**Say in interview**: *"Exact KNN is O(N) per query — infeasible at 1B vectors and 10K QPS. ANN reduces this to O(log N) by pruning the search space. We accept ~5% recall loss for 1000x speedup."*

---

#### 2. HNSW — the primary ANN algorithm to know
**What it is**: Hierarchical Navigable Small World. Builds a multi-layer graph where each vector is a node connected to its nearest neighbors.

**How it works**:
- Upper layers: sparse — few nodes, long-range connections (like a highway)
- Lower layers: dense — many nodes, short-range connections (like local roads)
- Query: start at top layer, greedily navigate toward query vector, descend to finer layers
- Think: highway system — take the highway to get close, local roads for the last mile

**Pros**: very fast queries O(log N), high recall, supports real-time incremental upserts
**Cons**: high memory (~300GB for 1B 768-dim vectors), slow initial build

**IVF-PQ alternative**: clusters vectors into K groups (K-means), searches only nearest clusters. Add Product Quantization to compress 8-32x. Lower memory, slightly lower recall. Better for billion-scale with memory constraints.

**Vertex AI uses ScaNN** — Google's own algorithm, similar to IVF-PQ with optimized distance computation.

**Say in interview**: *"HNSW per shard — graph-based, O(log N) query, high recall, supports incremental upserts. For billion-scale memory constraints, IVF-PQ trades some recall for 8-32x memory reduction via compression."*

---

#### 3. Sharding vs Leader/Follower
**Why leader/follower doesn't work**: a single node can't hold 1B vectors in memory. HNSW for 1B 768-dim vectors needs ~300GB — far beyond one node.

**The right pattern — sharding**:
```
Shard 0: vectors 0–200M
Shard 1: vectors 200M–400M
...
Shard 4: vectors 800M–1B
```

**Query fan-out**: broadcast to all shards in parallel → each returns local top-K → merger combines into global top-K.

**Write routing**: upsert goes to the shard responsible for that vector ID (consistent hashing).

**Replicas per shard**: 3 replicas for availability — but replication is secondary to sharding.

**Say in interview**: *"Sharding first — 1B vectors can't fit on one node. Fan-out queries to all shards in parallel, merge results. Replicate each shard 3x for availability."*

---

#### 4. Delta Index Pattern for Real-Time Upserts
**The problem**: rebuilding a billion-vector HNSW index takes hours. Can't do it on every upsert.

**The solution — delta index** (same pattern as LSM trees in Bigtable/RocksDB):
```
Write:      new vector → small in-memory delta index (fast to update)
Query:      search main index + delta index in parallel → merge results
Background: periodically merge delta into main index (every few minutes)
Deletes:    tombstone set → filter at query time → purged during merge
```

**Why it works**: delta index is small → HNSW updates are fast on small graphs. Queries search both → freshness within seconds. Background merge is offline → doesn't block queries. Upserts visible within 1 minute ✓

**LSM tree analogy**: fast writes to a small mutable memtable, periodic compaction into large immutable SSTables. Exact same pattern, different domain.

**Say in interview**: *"Delta index pattern — new vectors go to a small in-memory delta index, queries search both main and delta, background job merges periodically. Same pattern as LSM trees."*

---

#### 5. Metadata Filtering — three approaches
**The problem**: query says "top-K similar vectors WHERE category=sports". How do you combine vector similarity with attribute filters?

**Approach 1 — Post-filtering** (simplest):
- Run ANN → get top-1000 → apply filter → return top-K
- Fails when filter is rare (1% match) — ANN returns 0 matching results in top-1000

**Approach 2 — Pre-filtering** (most accurate):
- Apply filter first → run KNN on matching subset
- Fails when filter matches many vectors — back to exact KNN on 500M vectors

**Approach 3 — Hybrid bitmap** (production answer, what Vertex AI does):
- Build a bitmap index on metadata attributes (like a DB index)
- At query time: compute filter bitmap, use it to skip non-matching vectors during HNSW traversal
- Filter applied during graph traversal, not after → recall holds for any selectivity

**Say in interview**: *"Post-filtering is simple but breaks for rare categories. Production approach: bitmap index on metadata — filter applied during HNSW graph traversal so recall holds regardless of how selective the filter is."*
