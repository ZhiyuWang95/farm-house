# System Design: ML Feature Store

**Difficulty**: Hard
**Relevance**: Vertex AI Feature Store — foundational ML infra, asked at Google/Meta/Uber

---

## Problem Statement

Design a Feature Store — a centralized system for storing, sharing, and serving
ML features for both model training (offline) and real-time inference (online).

---

## Requirements to clarify (ask before designing)

- How many features? (hundreds vs. millions of feature values)
- Read pattern: batch training reads vs. low-latency online serving?
- Write pattern: streaming updates or batch ingestion?
- Point-in-time correctness required for training? (avoid label leakage)
- Feature sharing across teams?
- Consistency guarantees? (eventual vs. strong)

---

## Functional Requirements

- Register and manage feature definitions (schema, metadata)
- Ingest features in bulk (batch) and in real time (streaming)
- Serve features online at low latency for inference (< 10ms P99)
- Retrieve historical feature snapshots for training (point-in-time correct)
- Share features across teams and models

## Non-Functional Requirements

- Online serving: < 10ms P99 for single entity lookup
- Batch retrieval: support training sets of 100M+ rows
- High availability: 99.9%
- Consistency: eventual for online store, exact for training snapshots

---

## Your Design

### 1. High-Level Architecture

### 2. Online Store (low-latency serving)
(what storage? what access pattern?)

### 3. Offline Store (training data)
(what storage? how do you handle point-in-time correctness?)

### 4. Ingestion Pipeline
(batch and streaming paths)

### 5. Point-in-Time Correctness
(what is it and how do you guarantee it?)

### 6. Feature Registry
(how do teams discover and reuse features?)

### 7. Tradeoffs

---

## Mock Interview Notes (2026-07-06)

### What I got right
- Clarifying questions: feature source (batch vs streaming), multi-tenancy (caught unprompted — good senior instinct), API boundary
- Online vs offline separation: correct reasoning — different access patterns drive different storage designs
- Parquet/columnar storage for offline was right concept
- Point-in-time correctness: correct approach — store full history with timestamps, use event_timestamp for joins
- UTC standardization — good detail
- Two-timestamp schema (event_timestamp vs created_timestamp) — correct instinct

### What to sharpen — detailed

---

#### 1. Bigtable for Online Store (not DynamoDB, not OpenSearch)
**What it is**: Bigtable is Google's managed NoSQL wide-column store. Row key = entity_id, columns = feature values. All data in memory-mapped SSTs on fast SSDs → sub-millisecond reads.

**Why it's a great fit**:
- Access pattern is pure key-value: `get(user_id) → {feature_values}` — no search, no complex queries needed
- Handles millions of QPS with consistent low latency (< 10ms P99 easily)
- Scales to petabytes — can store feature history for billions of entities
- Native GCP integration — Vertex AI Feature Store uses Bigtable under the hood

**Why not OpenSearch**: OpenSearch is a search engine optimized for full-text search and complex queries. For a simple `get by ID` lookup it's massive overkill — slower, more expensive, harder to operate.

**Why not DynamoDB**: Correct pattern (key-value), but DynamoDB is AWS. In a Google interview always use GCP equivalents: Bigtable = DynamoDB equivalent on GCP.

**Schema**:
```
row key:  user_123
columns:  spend_30d=450.0, age=32, last_login_ts=1720123456
```
Only stores **latest value** per feature — no history (history lives in offline store).

**Say in interview**: *"Bigtable for online store — row key is entity_id, columns are feature values. Sub-millisecond reads, scales to petabytes, this is exactly what Vertex AI Feature Store uses under the hood."*

---

#### 2. BigQuery for Offline Store (not raw S3/GCS)
**What it is**: BigQuery is Google's serverless columnar data warehouse. Stores data in columnar Parquet-like format, SQL-queryable, scales to petabytes, optimized for analytical scans over large datasets.

**Why it's a great fit**:
- Training jobs need to scan 100M+ rows with time-based filters — columnar storage makes this fast (only reads the columns you need)
- SQL support makes point-in-time joins easy to express and execute
- Partition pruning on `event_timestamp` means queries only scan relevant time ranges
- Serverless — no cluster to manage, scales automatically
- Native integration with Vertex AI Pipelines and training jobs

**Why not raw GCS/S3 + Athena**: Works, but you'd have to manage partitioning, file formats, and query optimization yourself. BigQuery handles all of this natively and is the standard answer on GCP.

**Schema**:
```
entity_id | feature_name | value  | event_timestamp      | created_timestamp
user_123  | spend_30d    | 450.0  | 2026-01-15 10:30:00  | 2026-01-15 10:35:00
user_123  | spend_30d    | 380.0  | 2026-01-10 09:00:00  | 2026-01-10 09:05:00
```

**Say in interview**: *"BigQuery for offline store — columnar so training scans are fast, SQL makes point-in-time joins easy, partitioned on event_timestamp for pruning. This is the standard GCP answer."*

---

#### 3. Late-Arriving Data and the Two-Timestamp Problem
**What it is**: Features don't always arrive in real time. An event at 10am might not reach the store until noon due to pipeline delays, retries, or backfill jobs.

**The two timestamps**:
- `event_timestamp`: when the real-world event happened (the truth)
- `created_timestamp`: when it was written to the store (system time)

**Why this matters**: if a training job runs at 11am, it never sees the feature that arrived at noon — even though that feature's event happened at 10am (before the label). The training dataset has a silent gap.

**The fix**:
1. Always store both timestamps
2. After late data arrives, query `created_timestamp` to find which training jobs ran during the gap
3. Recompute affected training rows using the now-complete data

**Why point-in-time correctness still holds**: you use `event_timestamp <= label_timestamp` for correctness — late arrival doesn't corrupt existing training data, it just means some rows were missing until the recompute.

**Say in interview**: *"I store both event_timestamp and created_timestamp. Event_timestamp drives point-in-time joins. Created_timestamp lets me detect late-arriving data and trigger recomputation of affected training snapshots."*

---

#### 4. Point-in-Time Join — the core query
**What label leakage is**: using features from AFTER the label event to train the model. The model sees future data it can't see in production → looks good offline, fails in production.

**The fix — point-in-time join**:
```sql
SELECT l.user_id, l.label, f.value
FROM labels l
JOIN feature_history f
  ON l.user_id = f.entity_id
  AND f.feature_name = 'spend_30d'
  AND f.event_timestamp = (
      SELECT MAX(event_timestamp)
      FROM feature_history
      WHERE entity_id = l.user_id
      AND feature_name = 'spend_30d'
      AND event_timestamp <= l.label_timestamp  -- THE critical line
  )
```

`<= label_timestamp` is the one line that prevents leakage. Every feature lookup is anchored to its label's time.

**Say in interview**: *"Point-in-time join: for each training label at time T, fetch the most recent feature value where event_timestamp <= T. The <= is what prevents label leakage."*
