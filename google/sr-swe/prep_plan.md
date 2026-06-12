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

## Starting confidence (self-rated /5)
| Area | Rating | Notes |
|---|---|---|
| Coding/Algorithms | 1.5 | Python, knows concepts but rusty, target medium+ |
| System Design | 3.5 | solid foundation |
| K8s | 2 | hands-on before, not recently. HM flagged etcd/internals debugging |
| AI/ML Infra | 3 | inference systems, dataloaders, large-scale inference libs. HM flagged multi-GPU LLM sharding |
| Behavioral | 4 | strong |

## Hiring Manager Signals
- Deep K8s knowledge required — debugging etcd / internal K8s components
- Asked about sharding a large LLM across multiple GPUs (model/tensor parallelism) — candidate noted this as a gap

## Note on "Infrastructure/Kubernetes background and experience" round
Round 4 was renamed from "K8s context" to this — likely a resume/experience deep-dive
("walk me through your K8s/infra work") rather than abstract internals trivia.
HM's etcd/internals comment likely surfaces as follow-up probing based on what you
mention. Prep priority: build a concrete inventory of past K8s/infra projects with
"depth-ready" talking points — for each, be ready to go 2-3 levels deeper if pushed
(e.g., "I debugged a scheduling issue" -> be ready to discuss scheduler internals,
node affinity/taints, what logs/tools you used, etc.).

---

## Week 1 (Jun 10 - Jun 16): Foundations & Diagnostics

### Coding (daily, ~45-90 min, untimed — focus on pattern recognition)
- [ ] Arrays/Strings/Hashmaps — two pointers, sliding window (4-6 problems)
- [ ] Linked Lists, Stacks/Queues, Binary Search
- [ ] Trees, BFS/DFS, intro to 1D DP

### K8s (3 sessions, ~45-60 min)
- [ ] Control plane architecture refresh: API server, etcd, scheduler, controller manager
- [ ] Node components: kubelet, kube-proxy, container runtime, pod lifecycle
- [ ] etcd basics: data model, watch mechanism, how API server uses it

### AI/ML Infra (2 sessions)
- [ ] Inventory current inference-system experience — write up what you've built
- [ ] GPU memory math: model size, activation memory, KV cache sizing
- [ ] Intro: data parallelism vs model parallelism (tensor vs pipeline)

### System Design (1 session, weekend)
- [ ] Review framework/approach for Google-style design interviews
- [ ] 1 warm-up design problem to gauge current level

### Behavioral (1 session, weekend)
- [ ] Brainstorm 6-8 STAR stories: leadership, conflict, ambiguity, technical decisions, failure/learning, customer focus, mentorship, cross-team collaboration

---

## Week 2 (Jun 17 - Jun 23): Deep Dives

### Coding (daily, timed 25-35 min/problem)
- [ ] Graphs: BFS/DFS, topological sort, Union-Find
- [ ] DP: 2D, knapsack patterns
- [ ] Heaps/Priority Queues, Greedy
- [ ] 1 mock coding interview (end of week)

### K8s (2-3 sessions)
- [ ] etcd deep dive: Raft basics, watch/revision model, performance tuning, failure modes (disk latency, defrag, quorum loss)
- [ ] Controller pattern: reconciliation loops, informers/listers/workqueues, operators
- [ ] Debugging toolkit: kubectl debug, crictl, common failure scenarios (CrashLoopBackOff, OOMKilled, pending pods)

### AI/ML Infra (2 sessions)
- [ ] Multi-GPU parallelism deep dive: tensor/pipeline parallelism, ZeRO/FSDP
- [ ] Inference-side: tensor-parallel serving (vLLM/TensorRT-LLM), continuous batching, KV cache management
- [ ] GKE + AI/ML: GPU/TPU node pools, device plugins, multi-host (JobSet, LeaderWorkerSet)

### System Design (1 session)
- [ ] 1 full design problem (infra/cloud-relevant), mock + feedback

### Behavioral (1 session)
- [ ] Practice delivering 3-4 stories, refine STAR structure

---

## Week 3 (Jun 24 - Jun 30): Mock Interviews & Integration

### Coding (daily, timed)
- [ ] Mixed-topic mediums + occasional hard
- [ ] 2 mock coding interviews

### K8s (2 sessions)
- [ ] GKE-specific: Autopilot vs Standard, autoscaling (CA/HPA/VPA), networking (VPC-native, Workload Identity, Gateway API)
- [ ] Mock K8s context interview — scenario-based debugging

### AI/ML Infra (1-2 sessions)
- [ ] Practice "shard a large LLM across GPUs" question + variants
- [ ] End-to-end: architect an AI/ML workload on GKE

### System Design (1-2 sessions)
- [ ] 1-2 more designs, mock + feedback

### Behavioral (1 session)
- [ ] Full mock behavioral interview

---

## Week 4 (Jul 1 - Jul 5): Polish & Final Mocks
- [ ] Full mock loop simulation (all 5 interview types)
- [ ] Targeted review of weak spots from mocks
- [ ] Taper down — light review only by Jul 4-5, avoid burnout

---

## Folder Map
- `coding/` — problem sets, solutions, pattern notes
- `design/` — system design practice writeups
- `behavior/` — STAR story bank
- `domain_knowledge/` — K8s internals notes, AI/ML infra notes
