# System Design: LLM Inference Serving Platform

**Difficulty**: Hard
**Relevance**: Vertex AI core product — Model Garden, Vertex AI Prediction, MaaS

---

## Problem Statement

Design a low-latency, high-throughput serving platform for large language models (LLMs).
The system should serve multiple models to external partners/customers via an API,
handle bursty traffic, and keep costs efficient.

---

## Requirements to clarify (ask before designing)

- What models? (sizes: 7B, 70B, 400B+ parameters)
- Latency targets? (time-to-first-token, end-to-end)
- Throughput? (requests/sec per model)
- Multi-tenancy? (one model shared across customers, or dedicated deployments)
- Streaming responses? (token-by-token vs. complete response)
- SLA guarantees? (99th percentile latency, uptime)

---

## Functional Requirements

- Clients send a prompt, receive a generated text response
- Support streaming (token-by-token) and batch responses
- Multiple model versions deployed simultaneously
- Per-customer quota enforcement
- Model hot-swap without downtime

## Non-Functional Requirements

- P50 TTFT < 500ms, P99 TTFT < 2s
- 10,000 concurrent requests across all models
- 99.9% availability
- Cost-efficient GPU utilization

---

## Your Design

### 1. High-Level Architecture

(draw/describe the major components and data flow)

### 2. Request Path (step by step)

(from client API call to token response)

### 3. Model Serving Layer

(how are models loaded? how is GPU memory managed?)

### 4. Scaling Strategy

(how do you handle traffic spikes?)

### 5. KV Cache Management

(what is it, why does it matter, how do you manage it?)

### 6. Multi-tenancy & Quota

(how do you isolate customers and enforce rate limits?)

### 7. Bottlenecks & Tradeoffs

(what are the hardest parts?)

---

## Mock Interview Notes (2026-07-06)

### What I got right

- Clarifying questions: model size, multi-tenancy, latency targets, throughput + spike ratio — comprehensive
- High-level architecture: API Gateway → auth/quota → model router → load balancer → autoscaling fleet
- Streaming: correct reasoning (UX + cancel-early efficiency); learned SSE for external, gRPC internally
- Quota: counter-based approach was right; needed prompting to name **Redis** specifically
- Cold start: identified two steps (download + GPU load); artifact caching (pre-baked disk snapshot) was correct
- Autoscaling metric: queue depth is correct
- Cost reduction: batching + exact-match caching — correct concepts

### What to sharpen — detailed

---

#### 1. Redis for Quota Enforcement
**What it is**: In-memory key-value store. All data lives in RAM → sub-millisecond reads/writes, orders of magnitude faster than any disk-based database.

**Why it's a great fit**: At 4,000 QPS during spikes, quota check must complete in < 1ms or it becomes the bottleneck. Disk-based DBs (Spanner, Postgres) have 5-20ms latency — that alone blows your P99 budget. Redis handles 100K+ ops/sec on a single node.

**The pattern — token bucket**:
```
key:   quota:{customer_id}:{current_minute}
op:    INCR  (atomic — no race condition at high concurrency)
check: if new_count > quota_limit → return 429
TTL:   2 minutes (auto-resets counter, no cleanup job needed)
```

**Failure mode**: if Redis goes down → fail open (allow requests). Overage is a billing problem; dropping traffic breaks SLA — worse outcome.

**Say in interview**: *"Redis for quota — in-memory so sub-millisecond, atomic INCR + TTL implements a sliding window counter with no race conditions, handles 100K ops/sec easily."*

---

#### 2. KV Cache + Prefix Caching — proactively bring this up
**What KV cache is**: During generation, the model computes Key and Value tensors for every token in the context. These are expensive. KV cache stores them so they aren't recomputed on every new token. Without it, generating token N would redo all work from tokens 1 to N-1.

**Why it matters for system design**: KV cache consumes GPU VRAM proportional to sequence length × batch size. It is the #1 GPU memory bottleneck — it directly limits how many concurrent requests a node can serve.

**Prefix caching**: If 1,000 requests share the same system prompt, their KV tensors for that prompt are identical. Compute once, reuse for all. Vertex AI and vLLM both support this natively.

**Connection to load balancing**: Routing same-prefix requests to the same node (sticky routing) keeps the prefix KV cache warm — skips recomputation entirely. This is why round-robin fails: it scatters same-prefix requests across nodes.

**Say in interview**: *"KV cache is the key LLM-specific bottleneck — limits concurrency per node. I'd use prefix caching for shared system prompts and sticky routing to maximize cache hits."*

---

#### 3. LOR Routing (Least Outstanding Requests)
**What it is**: Route each new request to the node with the fewest currently in-flight requests, rather than cycling round-robin.

**Why round-robin fails**: LLM requests vary wildly — 1s for a short response, 30s for a long one. Round-robin is blind to this and piles work onto slow nodes while others sit idle.

**Why LOR works**: Fewer in-flight requests = more GPU capacity available right now. Load-aware without needing to predict request duration.

**Combined strategy**: LOR for load distribution + prefix-aware sticky routing for KV cache reuse.

**Say in interview**: *"LOR instead of round-robin — LLM requests range from 1s to 30s so round-robin creates hot nodes. LOR routes to least-loaded node; combine with sticky routing for KV cache reuse."*

---

#### 4. Continuous Batching
**What it is**: Static batching waits for N requests before running the GPU — adds queuing latency, leaves GPU idle. Continuous batching inserts new requests into an in-flight generation step between token iterations. GPU never idles.

**Why it's a great fit**: GPU utilization is the direct cost driver. Higher utilization = more tokens per dollar. This is the core of vLLM — why it became the de facto serving engine.

**Say in interview**: *"Continuous batching (vLLM) — inserts new requests between token steps so GPU never idles. This is the main lever for GPU utilization."*

---

#### 5. SSE vs gRPC for Streaming
**SSE (Server-Sent Events)**: HTTP-based, server pushes `data: {token}\n\n` chunks, works in any browser, no special client library. Best for external customer-facing API.

**gRPC server-side streaming**: `rpc Generate(Request) returns (stream TokenResponse)` — strongly typed, better performance, requires gRPC client. Best for internal service-to-service.

**Say in interview**: *"SSE externally — universal browser support, simple. gRPC streaming internally — better performance and type safety."*

