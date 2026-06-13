# Cloud AI — Vertex Prediction MaaS: Opportunity Notes

## Situation (as of 2026-06-12)
Recruiter Brandon surfaced a second opportunity: Senior Software Engineer, Cloud AI
— Vertex Prediction MaaS team. This is **in addition to**, not instead of, the
ongoing GKE Customer Success process (`../sr-swe/prep_plan.md`) — Brandon confirmed
GKE "is still very much in effect."

- Framed as a "hiring sprint" with "different hiring practices" — likely a
  faster/less formal process than the standard 5-round GKE loop.
- Brandon offered to schedule an intro conversation with the team next week
  (week of 2026-06-15).
- No formal interview loop or dates yet.

## Availability
- **Jul 6-10**: unavailable — GKE interview loop (`../sr-swe/prep_plan.md`)
- **Jul 20-24**: next open stretch for a fuller MaaS loop, if the intro chat leads
  there quickly given the "hiring sprint" pace
- Week of Jun 15: open for the intro conversation Brandon proposed

Full JD/email text: `job_description/role_overview.md`.

## Update (2026-06-12): expedited slate
Brandon replied that this team uses an **expedited slate: 1 coding + 1 system
design** (vs. GKE's standard 5-round loop) — described as "very rare" for Google,
a "pilot" specific to this project. He asked whether this changes Joey's
availability.

**Implications**:
- No dedicated K8s/infra round — reinforces that K8s-internals depth (etcd etc.,
  the GKE HM's flag) is not central to this track.
- No dedicated behavioral round — the informal intro chat may be the only
  behavioral touchpoint.
- Coding prep is fully shared with GKE (`../sr-swe/coding/`) — zero extra lift.
- System design is now the dominant MaaS-specific prep surface —
  `design/maas_design_topics.md` is the highest-priority MaaS material.

**Decision (2026-06-12)**: both processes in the same week — the MaaS 2-round
loop (1 coding + 1 system design) will be proposed for the week of Jul 6,
alongside the GKE loop. GKE currently occupies Mon/Wed/Thu/Fri that week, leaving
Tuesday (Jul 7) open — proposed to Brandon as the likely slot, pending the MaaS
team's calendar.

**Prep implication**: Jul 6-10 is now a 6-interview week across two processes.
Given the heavy overlap (coding fully shared; MaaS system design overlaps with
AI/ML infra design), the main change is to fold ≥1 MaaS-flavored design prompt
(`design/maas_design_topics.md`) into the existing GKE system design practice
sessions — see `../sr-swe/prep_plan.md` Week 3.

## How this maps to existing GKE prep
Significant overlap with the AI/ML Infra track already planned for GKE prep weeks
2-3 (multi-GPU/LLM serving, KV cache management, vLLM/TensorRT-LLM, continuous
batching) — that work is directly transferable here.

**New/MaaS-specific areas** (not covered by GKE prep):
- Prefix caching & cache-aware routing as serving-layer optimizations
- Multi-tenant, partner-facing platform design (isolation, SLAs, billing/metering
  for monetization)
- Partner integration patterns — onboarding a new model provider onto a platform
- Vertex AI Model Garden / MaaS-specific framing (if public docs available)

K8s-internals depth (etcd, etc. — the GKE HM's flag) is likely **less central**
here; MaaS interviews probably skew toward serving-systems design and AI/ML infra
over K8s internals.

## Recommendations
1. **Take the intro chat** — low-cost optionality, especially given the
   "urgency"/faster-track framing. Reply to Brandon to schedule next week.
2. **Don't pause GKE prep** — it has firm dates (Jul 6-10) and remains the primary
   track; continue `../sr-swe/prep_plan.md` as planned.
3. **Lean into the overlap** — the AI/ML Infra deep-dive (multi-GPU parallelism,
   inference serving, KV cache) serves both tracks; no need to duplicate effort.
4. **Light prep for MaaS-specific gaps** (as time allows, lower priority until a
   loop is scheduled): prefix caching/cache-aware routing, multi-tenant platform
   design, partner-onboarding patterns.
5. **Watch for schedule overlap** — if the "hiring sprint" moves fast, be mindful
   of conflicts with the Jul 6-10 GKE loop when coordinating with Brandon.
6. **Behavioral**: existing STAR bank (`../sr-swe/behavior/`) is largely reusable;
   consider reframing 1-2 stories toward partner-facing / multi-consumer platform
   work for this track specifically.

## Folder map
- `job_description/` — Brandon's email + JD details
- `domain_knowledge/` — MaaS-specific serving/platform topics
- `design/` — MaaS-flavored system design practice
- `behavior/` — pointer to shared STAR bank + MaaS-specific reframings
- Coding prep is shared — see `../sr-swe/coding/`
