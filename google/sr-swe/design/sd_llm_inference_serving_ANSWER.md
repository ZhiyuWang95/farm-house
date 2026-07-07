# System Design: LLM Inference Serving Platform — ANSWER

---

## Clarifications to establish upfront

- Model sizes: mix of 7B–70B (single GPU), 400B+ (multi-GPU tensor parallel)
- Streaming required: yes (token-by-token via SSE/gRPC)
- Multi-tenant: yes, shared model instances across customers
- Quota: per-customer tokens/min rate limit
- Latency target: P50 TTFT < 500ms, P99 < 2s

---

## High-Level Architecture

```
Client
  │
  ▼
API Gateway  ──── Auth / Quota enforcement (Redis token bucket)
  │
  ▼
Request Router  ── model version routing, load balancing
  │
  ▼
Inference Fleet (GPU nodes)
  ├── Model Server (vLLM / TensorRT-LLM)
  │     ├── Continuous batching engine
  │     └── KV cache manager (PagedAttention)
  └── Autoscaler  ◄── Prometheus metrics (queue depth, GPU util)
  │
  ▼
Response Streamer  ── SSE / gRPC streaming back to client
```

---

## Request Path

1. Client sends POST `/v1/generate` with `{model, prompt, params}`
2. API Gateway authenticates, checks quota (Redis token bucket per customer)
3. Router selects least-loaded replica for the requested model version
4. Inference server adds request to **continuous batch** (doesn't wait for batch to fill)
5. Model generates tokens; each token streamed back via SSE as produced
6. When EOS token or max_tokens reached, connection closes

---

## Model Serving Layer

**Key insight**: LLMs are memory-bandwidth bound, not compute bound during generation.

- **Loading**: models pre-loaded into GPU VRAM at startup; model weights pinned
- **Large models (400B+)**: tensor parallelism across multiple GPUs (split weight matrices across devices, all-reduce between layers)
- **Continuous batching**: instead of waiting for a full batch, new requests are inserted into in-flight batches between token generation steps — dramatically improves GPU utilization vs. static batching
- **Framework**: vLLM or TensorRT-LLM handle all of this; in an interview mention you'd use one of these rather than building from scratch

---

## KV Cache Management (PagedAttention)

**What it is**: During generation, the model computes key/value tensors for every token in the context. These are cached to avoid recomputation on subsequent tokens.

**The problem**: KV cache grows with sequence length and number of concurrent requests. Naive allocation (reserve max_seq_len per request) wastes memory.

**PagedAttention** (vLLM): treats KV cache like OS virtual memory — allocates in fixed-size pages, only as needed. Allows:
- More concurrent requests in the same VRAM
- Cache sharing between requests with identical prefixes (e.g. same system prompt)
- Prefix caching: if 1000 customers use the same system prompt, compute KV cache once, share it

**Interview talking point**: "KV cache is the primary GPU memory bottleneck for inference. PagedAttention is the key innovation that enables high-concurrency serving — it's why vLLM became the de facto serving engine."

---

## Scaling Strategy

**Vertical**: larger GPU instances (A100 80GB → H100 80GB) for bigger models or more VRAM for KV cache

**Horizontal**:
- Autoscaler watches: queue depth, GPU utilization, P99 TTFT
- Scale out replicas when queue depth > threshold
- Scale in slowly (avoid thrashing) — use stabilization windows
- Cold start latency is high (model loading takes 30-120s for large models) → keep minimum replicas warm

**Traffic shaping**:
- Request queue per model with priority lanes (streaming vs. batch)
- Shedding: return 429 when queue exceeds max depth rather than letting latency spike

---

## Multi-tenancy & Quota

- **Quota enforcement**: Redis token bucket per (customer_id, model) — deducted at gateway before routing
- **Isolation**: shared model instances (cost-efficient); dedicated instances only for enterprise SLA tiers
- **Fairness**: weighted fair queuing inside the inference server — prevent one customer's long-context requests from starving others
- **Billing**: count output tokens (more expensive than input for generation workloads)

---

## Bottlenecks & Tradeoffs

| Bottleneck | Approach |
|---|---|
| GPU memory limits concurrency | PagedAttention, prefix caching |
| Cold start latency on scale-out | Keep warm replicas, pre-warm on traffic forecast |
| Long-context requests starve short ones | Priority queues, max_context limits per tier |
| Multi-GPU coordination overhead | Minimize tensor parallel degree; prefer larger single GPUs |
| Model version rollout | Blue/green: run old + new in parallel, shift traffic gradually |

---

## Vertex AI Angle

- **Vertex AI Prediction** is essentially this architecture
- **Model Garden** adds model discovery and one-click deployment
- **Dedicated vs. shared endpoints**: maps to isolated vs. multi-tenant serving
- Mention **TPUs** as an alternative to GPUs for Google's own models (better perf/cost for transformer workloads at Google scale)

---

## Follow-up questions Google commonly asks

1. "How would you handle a 10x traffic spike in 2 minutes?" → pre-provisioned warm capacity + request queuing + graceful degradation
2. "How do you do a zero-downtime model update?" → blue/green with traffic shifting
3. "How would you reduce cost by 50%?" → spot/preemptible GPUs for batch, prefix caching, smaller distilled models
4. "How does streaming work under the hood?" → SSE: server sends `data: {token}\n\n` chunks; gRPC: server-side streaming RPC
