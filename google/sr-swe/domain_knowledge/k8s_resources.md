# K8s Study Resources

## Assessment: KodeKloud "100 Days of MLOps" (revised after seeing full curriculum)

Full breakdown of the 100-day plan:

| Days | Topic area | K8s-relevant? |
|---|---|---|
| 1-49 | Python/ML project setup, DVC, MLflow, training/tuning (Optuna/FLAML/PyTorch), feature stores (Feast), Vault, Great Expectations | No |
| 50-66 | Docker images (training/serving/GPU), model serving (Flask/FastAPI/BentoML), A/B & canary | Indirect (containers, not K8s) |
| 67-84 | Monitoring (Prometheus/Grafana/Evidently), CI/CD pipelines | No |
| 85-96 | Argo Workflows/Prefect, deploy on K8s, HPA, **KServe InferenceService**, Kubeflow, ArgoCD GitOps | **Yes** |
| 97-100 | Capstones (integrate everything) | Partial |

**Only ~12 of 100 days (85-96) are K8s-specific**, and even those are "K8s for ML
serving/orchestration" (KServe, HPA, GitOps) rather than K8s internals/architecture.
None of it covers etcd, building a CRD/controller from scratch, RBAC, scheduler, or
networking internals — exactly the areas the HM flagged, and what we dug into in the
`PlutoService` sessions (see `k8s_experience_inventory.md`).

### Revised recommendation
Given Round 4 = infrastructure/K8s background and experience (not AI/ML domain), this
curriculum is actually a better match for the round that *isn't* the focus.

- **Don't abandon it** — Days 92-96 give real K8s-on-K8s hands-on reps (KServe is a
  great parallel to `PlutoService`: it's also a CRD with a controller behind it), and
  the broader MLOps context is decent general background.
- **But it's no longer the primary K8s prep.** Higher-leverage use of time:
  1. Deepen the `PlutoService` action items (`k8s_experience_inventory.md`)
  2. K8s internals fundamentals (etcd, controllers/CRDs, RBAC, scheduler,
     networking) via "Kubernetes the Hard Way" + official docs (below)
  3. If time allows, KodeKloud days 92-96 specifically

---

## Assessment: CKAD vs CKA (Udemy/KodeKloud, Mumshad Mannambeth)

Joey was taking the **CKAD** (Certified Kubernetes Application Developer) course —
question was whether it covers control-plane/etcd internals, and whether **CKA**
(Certified Kubernetes Administrator) is the better fit.

Per official CNCF exam domain weights:

| Course | Focus | Relevant domains |
|---|---|---|
| CKAD | "developer using a cluster someone else manages" | App Design/Build, Deployment, Observability, Config/Security, Networking — Pods, probes, ConfigMaps/Secrets, SecurityContext. Assumes cluster already exists. |
| CKA | "cluster admin" | **Cluster Architecture, Install & Config (25%)** — control plane components, RBAC, **etcd backup/restore**, kubeadm bootstrapping. **Troubleshooting (30%)** — control plane / worker node / network failure debugging. |

**CKA is the better-aligned course for the HM's "etcd / internal components" flag** —
its Cluster Architecture and Troubleshooting modules are the closest thing to "what's
inside k8s" in this catalog.

**Recommendation given the timeline**: don't switch to the full CKA course (~20hrs,
cert not needed) — cherry-pick three modules:
1. **Cluster Architecture** — control plane components + how they talk to etcd
2. **ETCD** — including backup/restore labs (most hands-on etcd content available)
3. **Troubleshooting** — control-plane failure debugging

### Concrete course pick
[Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
— Mumshad Mannambeth/KodeKloud, the de facto standard CKA prep course (100k+
students, free browser-based labs included). Jump straight to **Cluster
Architecture → ETCD → Troubleshooting** (+ RBAC under Security) rather than doing
the course start-to-finish.

If partway through CKAD, it's not wasted (probes/ConfigMaps/Services = general
fluency, useful for the `PlutoService` conversation) — just don't expect it to reach
etcd/internals depth. The three CKA modules above are a better-targeted addition.

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
- **Coursera: "Architecting with Google Kubernetes Engine" specialization** (Google
  Cloud) — Foundations / Workloads / Production courses. Covers the GKE-specific
  list above directly, plus security/RBAC and production ops (monitoring, logging,
  troubleshooting) from GKE's angle. Optional/secondary to the CKA modules above,
  but the "Foundations" course alone is a good single addition if time allows —
  especially relevant given it's Google's own framing for a Google interview.

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
