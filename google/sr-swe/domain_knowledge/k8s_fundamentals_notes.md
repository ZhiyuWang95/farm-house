# K8s Fundamentals — Concept Notes

Running notes from Q&A coaching sessions, building toward Week 1's "control plane
architecture + etcd basics" prep (see `prep_plan.md`).

---

## CRD / API server / Controller / etcd relationship

**Database analogy:**
- **CRD (CustomResourceDefinition)** = a table schema definition. Applied once via
  `kubectl apply`, it registers a new resource *type* (its fields, validation rules)
  with the API server.
- **API server** = the database + REST/watch layer for *all* resources — built-in
  (Pods, Deployments) and custom (once a CRD registers them). Once registered, the
  API server **generically** handles CRUD, validation, and storage in etcd for the
  new type — no extra backend service required for this part.
- **CR instance** = a "row" — an actual object of the new custom type.
- **Controller/operator** = a separate watcher/worker process, NOT in the
  synchronous request path for CRUD on a CR. It's a *client* of the API server
  (like `kubectl`) that:
  1. Runs an **informer** — a watch subscription + local cache — on CR instances.
  2. Reacts to add/update/delete events via a **reconcile function**.
  3. Makes its own separate API calls back to the API server to create/update other
     resources (e.g., a ConfigMap).
- **etcd** = the only thing the API server talks to directly for storage. The
  watch mechanism that informers rely on is built on etcd's watch feature,
  proxied through the API server.

**Flow**: CRD (schema, one-time) -> API server (generic storage/serving) ->
controller (watches via informer, reconciles into other resources)

### Mapped onto Joey's platform (inference serving)
1. Team's CRD (e.g. `EndpointConfig`) registered once — defines schema for a user's
   endpoint exposure config.
2. User configures endpoint via frontend -> CR instance created/updated via API
   server -> stored in etcd.
3. Team's controller has an informer watching `EndpointConfig` CRs.
4. On change, reconcile function reads the CR spec and creates/updates a ConfigMap.
5. **Open question**: what consumes that ConfigMap and how does it pick up changes?
   (tracked in `k8s_experience_inventory.md`)

---

## RBAC (Role-Based Access Control)
Authorization layer: controls **who** (User/Group/ServiceAccount) can do **what**
(verbs: get/list/watch/create/update/delete/patch) on **which resources**, in a
namespace or cluster-wide.

- **ServiceAccount** — identity for a process/Pod (controllers run as one, not as
  a human user)
- **Role** (namespaced) / **ClusterRole** (cluster-scoped) — set of permission rules
- **RoleBinding** / **ClusterRoleBinding** — binds a Role/ClusterRole to a subject

For an operator/controller: ServiceAccount (identity) + ClusterRole (permissions
on its CRD + whatever native resources it creates) + ClusterRoleBinding (ties them
together).

**Debugging signal**: missing/wrong RBAC -> operator runs fine, CR gets created/
stored, but reconciliation silently fails with `Forbidden`/403 in the controller's
logs. Classic "operator exists but does nothing" symptom, distinct from the
"operator deployment deleted entirely" case.

---

## Liveness vs Readiness probes
(see `k8s_experience_inventory.md` for the debugging story this came from)
- **Liveness probe failure** -> kubelet kills + restarts the container -> repeated
  failures = `CrashLoopBackOff`
- **Readiness probe failure** -> pod marked `NotReady`, removed from Service
  endpoints, but **not** restarted
- Mnemonic: *readiness = ready for traffic (routing); liveness = is it alive
  (restarts)*
