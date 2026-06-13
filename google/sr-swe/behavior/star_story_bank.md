# STAR Story Bank (shared across both tracks)

Source: `Joe-resume-202606.pdf` (updated Jun 2026) + work history. Per
`../../cloud-ai-maas/behavior/notes.md`, this bank is shared — most stories
transfer directly to MaaS with light reframing toward "platform for partners."

Target categories (prep_plan.md Week 1): leadership, conflict, ambiguity,
technical decisions, failure/learning, customer focus, mentorship, cross-team
collaboration.

---

## 1. GPU Capacity Management System (Adobe Firefly, 2025-2026)
- **Categories**: Leadership, Cross-team collaboration, Technical decisions
- **Sketch**: Led (team of 4) an end-to-end system — time-series forecasting
  for daily GPU demand, an ops control plane, a self-serve UI, and a Grafana
  dashboard suite — to standardize GPU resource management across the org.
  Scaled supported simultaneous model launches from 5 to 20.
- **GKE angle**: GPU/TPU node-pool capacity planning + autoscaling — strong
  for the AI/ML Infra round and Round 4 (infra experience).
- **MaaS angle**: probably your **strongest MaaS story** — "platform for
  managing shared GPU/TPU capacity across multiple consumers" is close to
  MaaS's "build a platform for partners" mandate. Reframe "teams at Adobe" as
  "tenants with competing capacity needs."
- **Need from you**: what was *your* slice vs. the team's? Any concrete
  technical decision you personally drove (e.g., forecasting model choice,
  control-plane architecture)?

## 2. Founding Engineer — New Inference Server (Firefly Platforms, 2025-2026)
- **Categories**: Ambiguity, Technical decisions, (Leadership if you co-drove
  design)
- **Sketch**: As a founding engineer, built a framework-agnostic alternative
  to an overburdened production system — control plane, Redis-based request
  queue, custom scale-to-zero autoscaler, s5cmd-based parallel weight download
  sidecar, filesystem snapshots for cold-start reduction. Enabled self-serve
  multi-model deployment on K8s.
- **GKE angle**: very strong — K8s-native infra, autoscaling design,
  sidecar pattern, cold-start optimization are all directly relevant to
  Rounds 1-2 (coding/design) and Round 4 (infra).
- **MaaS angle**: "self-serve deployment platform for researchers" maps
  cleanly to "self-serve platform for partners" — strong candidate for
  reframing.
- **Need from you**: a specific *ambiguous* moment — e.g., a design decision
  where requirements weren't clear and you had to make a call (good for the
  "ambiguity" category specifically).

## 3. Agentic Media-Understanding Query Layer (Firefly Foundry, current)
- **Categories**: Customer focus, Technical decisions, Ambiguity (new/MVP)
- **Sketch**: Built an MVP agentic query layer (LangGraph) — an LLM + tool
  loop letting enterprise customers conversationally query transcriptions,
  shot detection, and frame analysis across media libraries.
- **GKE angle**: weaker direct tie unless discussing the underlying compute
  platform.
- **MaaS angle**: per memory note, this is your freshest "agent with platform
  potential" example — useful for MaaS system-design rounds even if the STAR
  story itself is still thin (project is new/ongoing).
- **Need from you**: since it's ongoing, frame as "what I designed and why"
  rather than "Result" — any early technical decision (tool design, agent
  loop structure) worth highlighting?

## 4. TAC Module Productization (Firefly Foundry, current)
- **Categories**: Cross-team collaboration, Technical decisions
- **Sketch**: Migrated the TAC (Transcription/Analysis/Captioning) module from
  a local Python prototype to the production compute platform, integrating it
  into an Airflow-orchestrated pipeline.
- **Need from you**: what broke or got hard during productionization (scaling,
  dependency conflicts, testing gaps)? That's the meat of a technical-decisions
  or even failure/learning story.

## 5. On-Call Standardization (Firefly Platforms)
- **Categories**: Mentorship, Cross-team collaboration, possibly
  Failure/Learning
- **Sketch**: Built runbooks, structured incident-note templates, and
  knowledge-sharing processes to improve incident-response consistency and
  reduce tribal-knowledge dependency.
- **Need from you**: was there a specific painful incident (slow response due
  to missing context) that *motivated* this? That incident itself could be a
  separate failure/learning story, with this as the "Result"/follow-up.

## 6. Financial Data Platform Migration (Amazon Stores Finance, 2021-2024)
- **Categories**: Leadership, Technical decisions
- **Sketch**: Led migration of a financial data processing platform to a
  serverless OLAP engine + Java workflow orchestrator + SQL modularization,
  cutting processing time from 2 hours to 5 minutes.
- **Need from you**: what alternatives did you consider/reject for the
  serverless OLAP choice? Any resistance to migrating a production finance
  pipeline (good conflict-angle candidate)?

## 7. Flexible Data Export Feature (Amazon Stores Finance)
- **Categories**: Ambiguity/Initiative, Technical decisions
- **Sketch**: Initiated and led a data-export feature with flexible
  granularity/aggregation, cutting processing time from 3 hours to under 10
  minutes via Java multi-threading.
- **Strength**: "initiated" = you identified the need yourself — good for the
  "ambiguity/initiative" category without needing much extra detail.

## 8. ML Inference Image Upgrade (Amazon Translate, AWS)
- **Categories**: Technical decisions, possibly Conflict
- **Sketch**: Led upgrade of core ML translate inference image — PyTorch,
  CUDA, and other key dependencies — through testing and production
  deployment.
- **Need from you**: upgrading core prod dependencies often meets pushback on
  timing/risk — was there a stakeholder disagreement here? If so, this could
  be your conflict story.

---

## Gaps — categories not yet well covered
- **Conflict**: no story above has a clear "I disagreed with X and here's how
  it resolved" arc yet. Best candidates to dig into: #8 (upgrade timing/risk
  pushback), #6 (resistance to migrating prod finance pipeline), or #1
  (competing GPU-capacity priorities across teams).
- **Failure/Learning**: nothing on the resume directly shows this (expected —
  resumes don't list failures). Best candidates: an on-call incident behind
  #5, or an early design choice in #2 that had to be reworked.

**Questions for you** (pick whichever has the most vivid memory attached):
1. For #8 or #6 — was there a real disagreement with a teammate/stakeholder
   about approach or timing? What was it, and how did it resolve?
2. For #5 — is there a specific incident (a bad on-call night, a slow
   triage) that motivated the runbook/template work?
3. For #2 — any early architectural choice (Redis queue, snapshot-based cold
   start, etc.) that didn't work as expected and had to change?
