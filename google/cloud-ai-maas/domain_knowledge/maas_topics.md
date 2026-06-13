# MaaS-Specific Domain Topics (to research once a loop is scheduled)

These are the gaps *not* already covered by the GKE prep's AI/ML Infra track
(multi-GPU parallelism, KV cache, vLLM/TensorRT-LLM, continuous batching — see
`../../sr-swe/domain_knowledge/`).

## Prefix caching & cache-aware routing
- What prefix caching is (reusing KV cache across requests sharing a common
  prompt prefix — system prompts, few-shot examples, RAG context)
- vLLM's `enable_prefix_caching`, SGLang's RadixAttention as concrete examples
- Cache-aware routing: load balancer routes requests to the replica most likely to
  already hold the relevant prefix in its KV cache — trade-off vs. plain
  round-robin/least-loaded balancing

## Multi-tenant, partner-facing platform design
- Isolation between tenants/partners (compute, data, billing) on shared
  infrastructure
- SLAs and quota/rate-limiting per partner
- Metering/billing for monetization (usage-based pricing for model creators)

## Partner/model onboarding pipelines
- What it takes to bring a new model (e.g., a new Anthropic or Mistral model) onto
  a serving platform: containerization/packaging, validation, capacity planning,
  versioning/rollout
- Supporting both open-source (e.g., Llama, Deepseek) and closed-source
  (Anthropic) models — different trust/IP boundaries

## Vertex AI / Model Garden framing
- Vertex AI Model Garden public docs — how Google currently frames MaaS
  externally, useful vocabulary and product framing for interviews
