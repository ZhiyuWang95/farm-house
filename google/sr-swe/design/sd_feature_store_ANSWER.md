# System Design: ML Feature Store — ANSWER

---

## Clarifications to establish upfront

- 500M+ feature values, 10K+ feature definitions across 50+ teams
- Online: single entity lookup at < 10ms P99 (real-time inference)
- Offline: batch retrieval of point-in-time correct snapshots for training
- Ingestion: both batch (hourly/daily) and streaming (sub-minute freshness)
- Point-in-time correctness: required (avoid training/serving skew and label leakage)

---

## High-Level Architecture

```
Producers (pipelines, streaming jobs)
  │                  │
  ▼ batch            ▼ streaming
Batch Ingestion    Stream Ingestion (Dataflow/Kafka)
  │                  │
  └─────────┬────────┘
            ▼
      Feature Store Core
      ┌─────────────────────────────┐
      │  Feature Registry (metadata)│
      │  Offline Store (GCS/BQ)     │  ← training, point-in-time snapshots
      │  Online Store (Bigtable/Redis)│ ← real-time serving
      └─────────────────────────────┘
            │                │
            ▼                ▼
      Training Jobs     Inference Services
      (batch read)      (online read < 10ms)
```

---

## Online Store

**Purpose**: serve features at inference time with < 10ms P99

**Storage**: Bigtable (Google) or Redis
- Row key: `entity_id` (e.g. user_id, item_id)
- Column: `feature_name → latest_value`
- Only stores the **latest** value per feature — no history

**Access pattern**: key-value lookup by entity_id, returns all features for that entity

**Why Bigtable over Redis**:
- Bigtable scales to petabytes; Redis is memory-limited
- Bigtable handles millions of QPS with consistent low latency
- Redis is acceptable for smaller scale or when sub-ms is required

**Serving API**:
```
GET /features?entity=user:123&features=[age, last_purchase_ts, spend_30d]
→ {age: 32, last_purchase_ts: 1720123456, spend_30d: 450.0}
```

---

## Offline Store

**Purpose**: historical feature data for model training — must be point-in-time correct

**Storage**: BigQuery (columnar, cheap, SQL-queryable) or Parquet on GCS

**Schema**:
```
feature_table: (entity_id, feature_name, value, event_timestamp, created_timestamp)
```

- `event_timestamp`: when the real-world event occurred (e.g. purchase time)
- `created_timestamp`: when the feature was written to the store (for late-arriving data)

**Retention**: keep full history — enables time-travel queries for any past snapshot

---

## Point-in-Time Correctness

**What it is**: When generating a training dataset, for each labeled event (e.g. "user churned on day T"), you must use only features that were available **before day T** — not future data. Using future data is label leakage and causes models that look good in training but fail in production.

**How to guarantee it**:

For each row in the training label set `(entity_id, label_timestamp)`:
```sql
SELECT entity_id, label_timestamp, f.value
FROM labels l
JOIN feature_table f
  ON l.entity_id = f.entity_id
  AND f.event_timestamp <= l.label_timestamp   -- only features known before label
  AND f.event_timestamp = (
    SELECT MAX(event_timestamp) FROM feature_table
    WHERE entity_id = l.entity_id
    AND feature_name = f.feature_name
    AND event_timestamp <= l.label_timestamp
  )
```

This is called a **point-in-time join**. Vertex AI Feature Store and Feast implement this natively.

**Interview talking point**: "Point-in-time correctness is the hardest part of a feature store. Without it, you get training/serving skew — the model sees future data in training that it can't see in production, leading to unrealistically good offline metrics but poor online performance."

---

## Ingestion Pipeline

**Batch path** (hourly/daily aggregates):
1. Spark/Dataflow job computes features from raw data (e.g. user spend in last 30 days)
2. Writes to both offline store (BigQuery) and online store (Bigtable)
3. Scheduled via Vertex AI Pipelines or Cloud Composer (Airflow)

**Streaming path** (sub-minute freshness):
1. Events arrive via Pub/Sub (e.g. real-time purchase event)
2. Dataflow streaming job computes features on-the-fly (sliding windows, counters)
3. Writes to online store immediately; writes to offline store for historical record
4. Offline store write includes exact event_timestamp for point-in-time correctness

---

## Feature Registry

**Purpose**: discoverability, reuse, governance across teams

**Stores**:
- Feature definitions (name, type, description, owner, entity type)
- Lineage (which pipelines produce it, which models consume it)
- Statistics (mean, variance, null rate — for data quality monitoring)
- Access control (which teams can read/write)

**Why it matters**: without a registry, team A computes "user age" differently from team B → duplicate computation, inconsistency. Registry enforces one definition, shared computation.

---

## Tradeoffs

| Decision | Option A | Option B | Choice |
|---|---|---|---|
| Online store | Redis (sub-ms, memory-limited) | Bigtable (ms, petabyte-scale) | Bigtable for scale |
| Offline store | BigQuery (managed, SQL) | Parquet/GCS (cheap, flexible) | BigQuery for ease of point-in-time joins |
| Freshness vs. cost | Streaming (fresh, expensive) | Batch (stale, cheap) | Both paths; choose per feature |
| Consistency | Strong (sync write to both stores) | Eventual (async to online) | Eventual ok; online store is best-effort latest |

---

## Vertex AI Feature Store specifics

- Vertex AI Feature Store uses Bigtable for online and BigQuery for offline natively
- `EntityType` = the thing being featurized (User, Item, Driver)
- `Feature` = one attribute of an EntityType
- `FeatureView` = materialized subset for serving (new in v2)
- Supports both streaming ingest (write_feature_values) and batch ingest from BigQuery

---

## Follow-up questions

1. "How do you detect training/serving skew?" → log feature values at inference time, compare distribution to training data distributions (monitor with statistics in registry)
2. "How do you handle late-arriving data?" → use `created_timestamp` vs `event_timestamp` separation; recompute affected training snapshots
3. "How do you version features?" → immutable feature definitions + versioned feature names (e.g. `user_spend_30d_v2`); old versions kept for model reproducibility
