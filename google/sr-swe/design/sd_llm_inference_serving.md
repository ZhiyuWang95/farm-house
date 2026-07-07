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
