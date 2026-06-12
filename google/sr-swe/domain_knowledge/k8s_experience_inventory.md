# K8s/Infra Experience Inventory

Tracks depth-ready talking points and research gaps for the
"Infrastructure/Kubernetes background and experience" round (Round 4, Jul 10).
Built incrementally via coaching sessions — see `prep_plan.md`.

---

## Project 1: ML Inference Serving Platform (Compute Platform team)

### Architecture (as understood so far)
- Researchers provide a model container image -> deployed as an inference service
  on the team's compute platform (built on K8s).
- Frontend: users configure how they want to expose their service (endpoint, path).
- Config is persisted to a DB AND reflected into a Custom Resource: **`PlutoService`**
  - Schema/types defined in `pluto_service_types.go`; CRD registered via
    `pluto_service.yaml`. API server handles CRUD/storage generically — no custom
    API code needed.
- Controller (`pluto_service_controller.go`, built by Joey's team) watches
  `PlutoService` CRs and reconciles them into:
  - a routing path for the endpoint
  - a ClusterIP Service
  - an `ExternalSecret` CR (for credentials — itself consumed by a separate
    external-secrets operator that produces the real K8s `Secret`)
  - a `.status` field (e.g. "Pending") reflecting reconciliation state
- Autoscaling: idle-time-based scale-to-zero (not queue-based) — tracks last
  request time, scales the pod to zero after a timeout (conceptually similar to
  Knative Serving's scale-to-zero).

### Depth-ready talking points (solid)
- [x] End-to-end pipeline: model image -> `PlutoService` CR -> controller ->
  Service/path/ExternalSecret -> endpoint
- [x] Reconciliation pattern: built a controller watching a CR, reconciling it into
  native K8s resources (own this story — directly relevant to "controller pattern"
  K8s topic)
- [x] **Core CRD/operator relationship** (strong): can articulate that the operator
  is what gives a CRD meaning — without it, `PlutoService` objects would still be
  accepted/stored by the API server, but nothing would act on them. Grounded in
  your own CRD + controller code.
- [x] Scale-to-zero design: idle-timeout-based vs. queue/request-rate-based (e.g. KEDA)

### Action items / gaps to research
- [x] ~~ConfigMap propagation mechanism~~ — superseded: controller creates a
  ClusterIP Service + routing path directly (native K8s objects), not just a
  ConfigMap. Standard K8s Service discovery (kube-proxy/CoreDNS) likely handles
  propagation here — revisit only if a gateway/ConfigMap step is still involved
  for the "path" piece.
- [ ] **ExternalSecret chain**: the controller creates an `ExternalSecret` CR for
  credentials. What operator (e.g. external-secrets.io) watches that and produces
  the real K8s `Secret`? This is a second concrete example of "operator gives a
  CRD meaning" — good for reinforcing the pattern with a different operator.
- [ ] **`.status` reconciliation state machine**: what are the possible values
  (Pending -> ? -> Ready/Failed)? What triggers each transition? Does the
  controller requeue/retry on failure (with backoff)? Has a `PlutoService` ever
  gotten stuck in "Pending" — and if so, how would/did you debug that?
- [ ] **"Last request time" tracking for scale-to-zero**: where is this tracked —
  a sidecar, a proxy in front of the pod, or a separate metrics pipeline? How does
  scale-from-zero handle the first incoming request (cold start / request buffering)?
- [ ] **Find one concrete CrashLoopBackOff instance** (see debugging story below) —
  a specific case with memorable details (what the probe config looked like, what
  the logs showed) would make this a much stronger STAR answer than the general
  pattern alone.

### Debugging Story: User Pod CrashLoopBackOff Triage
**Scenario**: Researchers deploy their model image onto the platform; sometimes the
image is broken (bad startup command, missing deps, wrong port, etc.) and the pod
enters `CrashLoopBackOff`. This is a recurring "is it the customer's problem or
ours" triage — core to the GKE customer-success role.

**Triage process**:
1. `kubectl describe pod` — check Events for probe failures / exit codes / reason
2. `kubectl logs` (and `--previous` for the crashed container) — find the
   application-level error
3. Identify whether it's a **liveness probe failure** (-> kubelet kills + restarts
   the container -> repeated failures = `CrashLoopBackOff`) vs. an application
   crash on startup vs. an OOMKill (exit code 137)

**Concept clarified during prep** (was initially reversed):
- **Liveness probe failure** -> container restarted -> `CrashLoopBackOff`
- **Readiness probe failure** -> pod marked `NotReady`, removed from Service
  endpoints, but **not** restarted
- Mnemonic: *readiness = ready for traffic (routing); liveness = is it alive
  (restarts)*

---
