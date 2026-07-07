# GKE Sr SWE Interview Prep Plan

## Overview
- **Role**: Senior Software Engineer, Infrastructure — GKE Customer Success (AI/ML focus)
- **Interview loop** (all times PDT, Los Angeles):
  - Mon Jul 6, 9:00-9:45am — Coding #1
  - Wed Jul 8, 9:00-9:45am — Coding #2
  - Thu Jul 9, 8:30-9:15am — System Design
  - Fri Jul 10, 8:00-8:45am — Infrastructure/Kubernetes background and experience
  - Fri Jul 10, 9:00-10:00am — Behavioral
- **Prep window**: Jun 10 - Jul 5 (~26 days)
- **Time budget**: 2-4 hrs weekdays, 5-6 hrs weekends (~20-32 hrs/week)

> **Note**: A second process (Cloud AI / Vertex MaaS, see `../cloud-ai-maas/`) is
> running in parallel and its 2-round loop (1 coding + 1 system design) is being
> proposed for Tuesday Jul 7 — making Jul 6-10 a 6-interview week across two
> processes. Coding prep is fully shared; system design practice below should
> include MaaS-flavored prompts (`../cloud-ai-maas/design/maas_design_topics.md`).

## Starting confidence (self-rated /5)
| Area | Rating | Notes |
|---|---|---|
| Coding/Algorithms | 1.5 | Python, knows concepts but rusty, target medium+ |
| System Design | 3.5 | solid foundation |
| K8s | 2 | hands-on before, not recently. HM flagged etcd/internals debugging |
| AI/ML Infra | 3 | inference systems, dataloaders, large-scale inference libs. **Not a GKE round** — relevant only to the parallel Vertex MaaS system-design round (see note below) |
| Behavioral | 4 | strong |

## Confirmed GKE round structure (as of 2026-06-21)
**5 rounds**: 2 coding, 1 K8s knowledge, 1 system design, 1 behavioral. No standalone AI/ML Infra round.

## Hiring Manager Signals
- Deep K8s knowledge required — debugging etcd / internal K8s components — covered in the **K8s knowledge** round.
- Asked about sharding a large LLM across multiple GPUs (model/tensor parallelism) — candidate noted this as a gap. **This is not part of the GKE K8s round.** It's prep surface for the parallel **Vertex MaaS** process's system-design round instead — keep it in System Design sessions, not K8s sessions.

## Note on "Infrastructure/Kubernetes background and experience" round
Round 4 was renamed from "K8s context" to this — likely a resume/experience deep-dive
("walk me through your K8s/infra work") rather than abstract internals trivia.
HM's etcd/internals comment likely surfaces as follow-up probing based on what you
mention. Prep priority: build a concrete inventory of past K8s/infra projects with
"depth-ready" talking points — for each, be ready to go 2-3 levels deeper if pushed
(e.g., "I debugged a scheduling issue" -> be ready to discuss scheduler internals,
node affinity/taints, what logs/tools you used, etc.).

---

## Revised compressed plan (as of 2026-06-21)

Original plan assumed ~20-32 hrs/week; actual available time is **2 hrs/weekday,
3-4 hrs/weekend** — only ~37.5 hrs total remain between today and 7/5. Re-prioritized
by round weight (coding = 2 of 5 GKE rounds, 40%) and confidence gap (coding 1.5/5,
weakest). AI/ML Infra is **not** a GKE round — it only shows up inside System Design
sessions (serves both GKE's design round and the likely Vertex MaaS design round).

**Progress so far**: Coding Day 1-3 done (`coding/problem_list.md`); K8s control-plane
basics (API server, etcd, scheduler/controller-manager split) covered in
`domain_knowledge/k8s_course_notes.md`. System Design, AI/ML, Behavioral: not started.

### Day-by-day: coding every other weekday (A), K8s + rotating partner the other (B)
| Date | Day | Focus |
|---|---|---|
| 6/22 Mon | A | Coding (full 2h — 1-2 timed problems + review) |
| 6/23 Tue | B | K8s (1h) + System Design review (1h) |
| 6/24 Wed | A | Coding |
| 6/25 Thu | B | K8s (1h) + Behavioral (1h) |
| 6/26 Fri | A | Coding |
| 6/27 Sat (3-4h) | — | System Design — full mock + feedback, include an AI/ML/MaaS-flavored prompt |
| 6/28 Sun (3-4h) | — | Coding mock (~1.5h) + Behavioral or K8s mock, rotating (~1.5-2h) |
| 6/29 Mon | A | Coding |
| 6/30 Tue | B | K8s (1h) + System Design review (1h) |
| 7/1 Wed | A | Coding |
| 7/2 Thu | B | K8s (1h) + Behavioral (1h) |
| 7/3 Fri | A | Coding |
| 7/4 Sat | — | Taper — light review only; 1 more System Design mock only if a real gap remains |
| 7/5 Sun | — | Taper — light review only, no new content, re-read STAR stories, rest |
| 7/6 Mon | — | **Interview Day 1 — Coding #1** |

### Checklist by area
**Coding**
- [x] Day 1-3 (`coding/problem_list.md`)
- [ ] Day 4 onward, ~3-4x/week pace (not literally daily) — pattern-focused first, timed 25-35 min/problem once warmed up
- [ ] 1-2 full mock coding interviews before 7/6

**K8s knowledge** (straight K8s — no AI/ML content here)
- [x] Control plane architecture: API server, etcd, scheduler, controller-manager (`domain_knowledge/k8s_course_notes.md`)
- [ ] Node components: kubelet, kube-proxy, container runtime, pod lifecycle
- [ ] etcd deep dive: Raft/quorum (done via quiz 6/21), watch/revision model, failure modes
- [ ] Debugging toolkit: kubectl debug, crictl, CrashLoopBackOff/OOMKilled/Pending scenarios
- [ ] GKE-specific: Autopilot vs Standard, autoscaling (CA/HPA/VPA), networking (VPC-native, Workload Identity, Gateway API)
- [ ] Build "depth-ready" inventory of past K8s/infra projects for the experience-style framing of this round

**System Design** (also covers AI/ML Infra content + MaaS overlap)
- [ ] Review framework/approach for Google-style design interviews
- [ ] 1-2 full mock design problems (infra/cloud-relevant)
- [ ] ≥1 mock including AI/ML-on-GKE or MaaS-flavored prompt (`../cloud-ai-maas/design/maas_design_topics.md`) — covers multi-GPU sharding, GPU/TPU node pools, KV cache, serving frameworks as content within the design discussion, not as standalone study

**Behavioral**
- [ ] Brainstorm 6-8 STAR stories: leadership, conflict, ambiguity, technical decisions, failure/learning, customer focus, mentorship, cross-team collaboration
- [ ] 1 full mock behavioral interview

---

## Folder Map
- `coding/` — problem sets, solutions, pattern notes
- `design/` — system design practice writeups
- `behavior/` — STAR story bank
- `domain_knowledge/` — K8s internals notes, AI/ML infra notes
