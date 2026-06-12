# K8s Study Resources

## Assessment: KodeKloud "100 Days of MLOps" / engineer.kodekloud.com/practice

(Couldn't load the live page — it's a JS app — but I know the platform well enough to assess it.)

**Good fit for:**
- Building genuine hands-on "I did X" experience — KodeKloud Engineer gives you real
  terminal/sandbox tasks (broken clusters, misconfigured services, etc.) rather than
  quizzes. This is exactly the kind of material that turns into credible stories for
  the **"infrastructure/Kubernetes background and experience"** round — "I had to
  debug a CrashLoopBackOff caused by X, here's how I traced it."
- General kubectl fluency, troubleshooting muscle memory, day-2 operations.

**Likely gaps relative to the HM-flagged areas** — keep doing KodeKloud, but
supplement with the items below:
1. **etcd internals** (Raft consensus, watch/MVCC, revision model) — task-based labs
   rarely go this deep; this is "explain how it works under the hood" knowledge.
2. **GKE-specific concepts** (Autopilot vs Standard, Workload Identity, VPC-native
   clusters, cluster autoscaler internals, GKE node auto-provisioning) — KodeKloud
   content tends to be vanilla/cloud-agnostic K8s.
3. **AI/ML-on-K8s specifics** (GPU/TPU scheduling, device plugins, multi-host
   training/inference primitives like JobSet/LeaderWorkerSet) — niche, unlikely to
   be covered.

Keep "100 Days" running for daily hands-on reps and experience-building — just don't
rely on it for the conceptual/internals depth below.

---

## Recommended Supplements

### etcd internals (HM explicitly flagged this)
- **etcd docs** (https://etcd.io/docs/) — data model, watch mechanism, Raft basics,
  MVCC/revisions. Read the "Learning" section.
- **Kubernetes the Hard Way** (https://github.com/kelseyhightower/kubernetes-the-hard-way)
  by Kelsey Hightower — manually bootstrapping etcd + control plane components is the
  single best way to internalize how the API server depends on etcd, how leader
  election works, and what happens when etcd is slow/unavailable.
- Kubernetes docs — Architecture/Components overview (https://kubernetes.io/docs/concepts/overview/components/)
  for how API server, scheduler, controller-manager, kubelet all interact via etcd's
  watch API.

### Controller / Operator patterns (reconciliation loops, informers, work queues)
- "Programming Kubernetes" (O'Reilly, Tremmel/De Smet) or the kubebuilder book —
  covers informers, listers, work queues, and the reconcile loop pattern that
  underlies almost every K8s controller.

### GKE-specific (likely under-covered by generic K8s resources)
- GKE docs (https://cloud.google.com/kubernetes-engine/docs) — focus on:
  - Autopilot vs Standard mode trade-offs
  - Cluster autoscaler / node auto-provisioning
  - Workload Identity, VPC-native clusters, Gateway API
  - GPU/TPU node pools, device plugins

### Debugging toolkit
- Kubernetes docs — Troubleshooting tasks (https://kubernetes.io/docs/tasks/debug/) —
  kubectl debug, crictl, common pod failure modes (CrashLoopBackOff, OOMKilled,
  ImagePullBackOff, pending/unschedulable pods).

---

## How this maps to prep_plan.md
- Week 1 K8s sessions: control plane architecture + etcd basics — use etcd.io docs +
  Kubernetes Architecture page.
- Week 2 K8s sessions: etcd deep dive (Raft/watch/failure modes) + controller
  patterns — Kubernetes the Hard Way + Programming Kubernetes.
- Week 3 K8s sessions: GKE-specific topics — GKE docs.
- Throughout: KodeKloud "100 Days" for daily hands-on reps that become "experience"
  talking points for Round 4.
