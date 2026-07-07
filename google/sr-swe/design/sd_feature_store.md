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
