# k8s architect

* kube-apiserver
    * central hub of the control plane — every component (kubectl, controllers, scheduler, kubelet) talks to the cluster only through it
    * authenticates incoming requests
    * handles admission control
    * validates objects and persists them to etcd

* kubectl
    * CLI client that sends requests to the API server

* etcd
    * cluster database
    * store the state of cluster
      * all cluster configuration
    * Never directly interact with etcd

* kube-scheduler
    * schedule pod onto the nodes
    * DO NOT do the work of actually launching pods on nodes. It chooses a node and writes the name of that node into the Pod object.
    * How does it decide where to run?
      * It knows the state of all the nodes.
      * it obeys constraints you define.
      * you can define affinity parameters.
      * you can also define anti-affinity parameters.

* kube-controller-manager
    * Continuously monitors the state of a cluster through the kube-apiserver.
    * It's called the controller-manager because many k8s objects are maintained by loops of code called controllers.
    * You can use certain kubernetes controllers to manage workloads.
    * Other types of controllers have system-level responsibilities.

* cloud-controller-manager
    * Manages controllers that interact with underlying cloud providers.

* On each node
    * kubelet: k8s agent on each node
        * kubelet watches the API server for pods scheduled to its node, then uses the container runtime to start the pod and monitors its lifecycle, including readiness and liveness probes.
        * Note: Container runtime is the software to launch a container from a container image.
        * (the API server also opens connections to kubelet for kubectl exec/logs/port-forward)
    * kube-proxy:
        * implements the Service abstraction — routes a Service's virtual IP to the right backend Pod IPs via iptables/IPVS rules.
        * Note: general pod-to-pod networking is handled by the CNI plugin (e.g. Calico, Cilium), not kube-proxy.

# etcd
* Distributed reliable key-value store

## etcd in k8s
* All kubectl get infos are from etcd cluster.
--advertise-client-urls: This is the address on which etcd listens.

You can setup etcd with 2 ways:
1. manual set up from scratch
2. set up with kubeadm

```
kubectl get pods -n kube-system
```

* To get all the keys in etcd, run this command:
```
kubectl exec etcd-master -n kube-system etcdctl get / --prefix -keys-only
>
/registry/apiregistration.k8s.io/apiservices/v1
```

* In the Highly available env, there are multiple master nodes, so multiple etcd.
It's important to set this `initial-cluster` configuration.

## (Optional) Additional information about ETCDCTL Utility

ETCDCTL is the CLI tool used to interact with ETCD.

ETCDCTL can interact with ETCD Server using 2 API versions - Version 2 and Version 3.  By default its set to use Version 2. Each version has different sets of commands.

For example ETCDCTL version 2 supports the following commands:
```
etcdctl backup
etcdctl cluster-health
etcdctl mk
etcdctl mkdir
etcdctl set
```

Whereas the commands are different in version 3
```
etcdctl snapshot save 
etcdctl endpoint health
etcdctl get
etcdctl put
```
To set the right version of API set the environment variable ETCDCTL_API command
```
export ETCDCTL_API=3
```


When API version is not set, it is assumed to be set to version 2. And version 3 commands listed above don't work. When API version is set to version 3, version 2 commands listed above don't work.



Apart from that, you must also specify path to certificate files so that ETCDCTL can authenticate to the ETCD API Server. The certificate files are available in the etcd-master at the following path. We discuss more about certificates in the security section of this course. So don't worry if this looks complex:
```
--cacert /etc/kubernetes/pki/etcd/ca.crt     
--cert /etc/kubernetes/pki/etcd/server.crt     
--key /etc/kubernetes/pki/etcd/server.key
```

So for the commands I showed in the previous video to work you must specify the ETCDCTL API version and path to certificate files. Below is the final form:


```
kubectl exec etcd-master -n kube-system -- sh -c "ETCDCTL_API=3 etcdctl get / --prefix --keys-only --limit=10 --cacert /etc/kubernetes/pki/etcd/ca.crt --cert /etc/kubernetes/pki/etcd/server.crt  --key /etc/kubernetes/pki/etcd/server.key" 
```

# Kube-apiserver
* Primary management component of Kubernetes — the central point of contact for the cluster.
* `kubectl` commands are just REST requests sent to the kube-apiserver; you can bypass kubectl entirely and POST to the API directly.

## Basic request flow
1. authenticate user
2. validate request
3. retrieve data
4. update etcd
5. scheduler
6. kubelet

It's actually the only component that interacts directly with the etcd data store.

## Example: creating a pod, end to end
1. Request (via `kubectl` or a direct POST) is authenticated, then validated.
2. API server creates the Pod object **without** assigning it to a node, writes it to etcd, and responds to the user that the pod was created.
3. kube-scheduler continuously watches the API server, notices a pod with no node assigned, picks the right node for it, and reports that back to the API server.
4. API server updates the pod's node assignment in etcd.
5. API server passes the pod spec to the kubelet on the assigned node.
6. kubelet creates the pod via the container runtime, then reports status back to the API server.
7. API server writes the updated status back to etcd.

Every change to the cluster follows this same pattern — kube-apiserver sits at the center of it, and all other components (scheduler, controller-manager, kubelet) go through the API server to read/write cluster state. None of them talk to etcd directly.

## Setup / configuration
* **kubeadm setup**: kube-apiserver runs as a static pod in the `kube-system` namespace on the master node, defined at `/etc/kubernetes/manifests/kube-apiserver.yaml`.
* **"Hard way" (non-kubeadm) setup**: kube-apiserver is a binary (from the Kubernetes release page) run as a systemd service on the master, configured via `/etc/systemd/system/kube-apiserver.service`.
* Either way, you can inspect the running process and its effective options with `ps -ef | grep kube-apiserver`.
* Most of the many startup options are certificates/keys used to secure connectivity between components — covered in detail later in the SSL/TLS certificates section.
* `--etcd-servers`: tells the kube-apiserver where to find the etcd cluster. This is the option that makes the API server *the* component that talks to etcd.

* View the apiserver options - kubeadm
```
cat /etc/kubernetes/manifests/kube-apiserver.yaml
```

# Quiz review — mistakes & gaps (2026-06-21)

## Q1: pod creation flow — what I got wrong
* **Scheduler does not watch etcd directly.** It only ever watches the **API server** for pods with no node assigned. No component except kube-apiserver talks to etcd directly — that's the entire point of the architecture.
* **There's no "controller" pulling the image and starting the pod.** That's the **kubelet** on the assigned node, talking to the container runtime. The scheduler's only job is to pick a node and report the binding back to the API server.
* Missing step: API server **authenticates + authorizes/validates** the request before writing anything to etcd.
* Corrected flow: `kubectl run` → API server (authn/authz/admission) → write Pod (no node) to etcd → respond to user → scheduler watches API server, picks a node → reports binding to API server → API server writes node assignment to etcd → API server pushes spec to kubelet on that node → kubelet + container runtime pull image, start container → kubelet reports status to API server → API server writes status to etcd.

### Controllers vs. bare pods
* `kubectl run` (modern kubectl, 1.18+) creates a **bare Pod** — no controller involved at all.
* `kubectl create deployment` involves controllers: Deployment controller (in kube-controller-manager) creates a ReplicaSet → ReplicaSet controller creates the Pod object(s) → from there it's identical to the bare-pod flow above.
* Controllers never bypass the API server or talk to nodes directly — every controller write goes back through kube-apiserver, same REST path a human would use.

## Q2: why kube-apiserver is the only etcd writer — what I got wrong
* My answer ("avoid polling for consistency") isn't the core reason — etcd already has a native watch/push mechanism, so polling isn't really the problem being avoided.
* Real reasons:
  1. **Security/authorization boundary** — kube-apiserver is the single chokepoint for authentication, RBAC authorization, and admission control (webhooks, quota checks) before any write. If kubelet/scheduler wrote to etcd directly, they'd need their own etcd certs, and a compromised node could write arbitrary cluster-wide state, bypassing RBAC entirely.
  2. **Abstraction over storage schema** — etcd is just an opaque KV store; it doesn't know what a "Pod" is. The API server owns object schema, defaulting, version conversion, and optimistic-concurrency (`resourceVersion` compare-and-swap). Direct writers would all have to agree on etcd's internal key layout/serialization, making the storage format impossible to change.

## Q4: etcdctl v2/v3 — what I got wrong
* `ETCDCTL_API` env var: already in notes above (line ~92-95) — `export ETCDCTL_API=3`. Default (unset) = v2.
* **Misconception**: I thought a missing `ETCDCTL_API` setting caused a kube-apiserver schema mismatch. Wrong — **etcdctl never goes through kube-apiserver at all.** The `kubectl exec etcd-master -n kube-system -- etcdctl ...` command gets a shell *inside the etcd pod* and talks directly to the local etcd server. This is the one sanctioned way to bypass the API server, used only for cluster-admin/debugging (snapshots, raw state inspection).
* **v2 and v3 are separate keyspaces/storage backends inside the same etcd process**, not just different schemas read through the same data. Kubernetes (via kubeadm) writes everything via v3. Running `etcdctl get` without `ETCDCTL_API=3` set queries the (empty, from k8s's perspective) v2 keyspace — so it silently returns nothing instead of erroring, because you're looking in the wrong storage namespace entirely.

## Q5 refresher: `initial-cluster`, Raft, and quorum (needed a full re-explanation)
* `initial-cluster` is a **bootstrap-only** etcd flag: a list of every member's name + peer URL (e.g. `etcd1=https://10.0.0.1:2380,etcd2=...`). Every member must start with the **same** list so they can find each other and elect a leader via Raft before any client (kube-apiserver) can read/write.
* **Failure mode avoided**: if the list is wrong/inconsistent across members, nodes fail to discover each other and each forms its **own** independent single-node cluster — a **split-brain**, with multiple disconnected etcd "clusters" instead of one with quorum, leading to divergent state depending on which instance a given kube-apiserver talks to.
* Adding/removing members after initial bootstrap uses `etcdctl member add/remove` + `--initial-cluster-state=existing` — reusing `new` on an already-formed cluster is a common way to accidentally trigger split-brain.

### Raft (consensus algorithm etcd uses)
* Node states: **Leader** (only one accepts writes, replicates to followers), **Follower** (passively replicates, sends heartbeats), **Candidate** (follower that timed out waiting for the leader, starts an election).
* Write flow: client → leader → leader appends to its log → replicates to followers → once a **majority** have it durably logged, leader marks it **committed** and acks the client.

### Quorum
* Quorum = majority of total members = `floor(N/2) + 1`. Cluster can only elect a leader / commit writes if a quorum is reachable.
  * 3 members → quorum 2 → tolerates 1 failure.
  * 5 members → quorum 3 → tolerates 2 failures.
  * 4 members → quorum 3 → **still only tolerates 1 failure** (same as 3-member) but slower writes — why etcd clusters are sized odd.
* **Quorum loss** = more than half the members down/unreachable at once → remaining nodes can't elect a leader or commit writes → entire control plane goes read-only/unavailable for writes until quorum is restored.

# Quiz Q&A — full review (2026-06-21)

**Q1. Walk through `kubectl run nginx` end to end, component by component.**
`kubectl run` → API server (authenticate → authorize → admission/validate) → write Pod object (no node assigned) to etcd → respond to user → kube-scheduler watches the **API server** (never etcd directly) for unscheduled pods, picks a node → reports the binding back to the API server → API server writes the node assignment to etcd → API server pushes the pod spec to the **kubelet** on that node → kubelet talks to the container runtime to pull the image and start the container → kubelet reports status back to the API server → API server writes status to etcd.
Modern `kubectl run` creates a bare Pod directly — no controller involved. (Contrast with `kubectl create deployment`: Deployment controller → creates ReplicaSet → ReplicaSet controller → creates Pod object(s) → same flow from there. Controllers only ever talk to kube-apiserver, never to nodes/scheduler directly.)

**Q2. Why is kube-apiserver the only component that talks to etcd directly?**
1. **Security/authz boundary** — single chokepoint for authentication, RBAC, and admission control before any write. If other components wrote to etcd directly they'd need their own etcd certs, and a compromised node could write arbitrary cluster-wide state, bypassing RBAC entirely.
2. **Abstraction over storage schema** — etcd is an opaque KV store with no concept of "Pod"/"Deployment". The API server owns object schema, defaulting, version conversion, and optimistic-concurrency (`resourceVersion` compare-and-swap). Direct writers would all need to agree on etcd's internal key layout, making the storage format impossible to evolve.

**Q3. How does the scheduler's node-assignment decision actually get written?**
Scheduler never writes to etcd. It posts the binding decision back to kube-apiserver (a `Binding` subresource call on the Pod), and kube-apiserver validates and persists it to etcd — same write path as any other update.

**Q4. etcdctl API v2 vs v3 — what's the difference, what controls it, why does forgetting it silently fail?**
Env var: `export ETCDCTL_API=3` (default, if unset, is v2). `etcdctl` (via `kubectl exec` into the etcd pod) talks **directly to the local etcd server — it never goes through kube-apiserver.** v2 and v3 are separate keyspaces/storage backends inside the same etcd process; Kubernetes (via kubeadm) writes everything through v3. Forgetting to set `ETCDCTL_API=3` means your `get` queries the (empty, from k8s's perspective) v2 keyspace — it returns nothing and exits cleanly, not an error, because you're looking in the wrong storage namespace entirely.

**Q5. What is `initial-cluster` for, and what failure mode does it prevent?**
A bootstrap-only etcd flag listing every member's name + peer URL. All members must start with the **same** list so they can find each other and elect a Raft leader before any client can read/write. Getting it wrong/inconsistent across members causes **split-brain**: each node forms its own independent single-node "cluster" instead of one cluster with quorum, so different kube-apiservers could see divergent state depending on which etcd instance they reach. (Adding members later uses `etcdctl member add` + `--initial-cluster-state=existing` — reusing `new` on an already-formed cluster is a common way to trigger split-brain.)

**Raft, in brief:** nodes are Leader (only one accepts writes, replicates to followers) / Follower (replicates, heartbeats) / Candidate (timed-out follower starting an election). Write flow: client → leader → leader appends to log → replicates to followers → once a **majority** have it durably logged, it's committed and acked.

**Quorum, in brief:** `floor(N/2) + 1` of total members. 3 members → tolerates 1 failure; 5 → tolerates 2; 4 → still only tolerates 1 (same as 3) but slower — why etcd is sized odd. **Quorum loss** (majority down) makes the whole control plane unable to commit writes until quorum is restored.

**Q6. kube-controller-manager vs cloud-controller-manager — example controller in each, and why it belongs there.**
- kube-controller-manager: e.g. **Deployment controller** — only reads/writes Kubernetes API objects through kube-apiserver, zero knowledge of underlying infra. Same binary behavior on GKE, EKS, or bare metal.
- cloud-controller-manager: e.g. **Service/LoadBalancer controller** — calls a specific cloud vendor's API to provision real infrastructure (e.g. an actual GCP/AWS load balancer) when you create a `Service type=LoadBalancer`.
The split exists to keep Kubernetes core cloud-agnostic: each vendor ships its own cloud-controller-manager implementing `cloudprovider.Interface`, so vendor SDKs never get baked into core k8s. (The distinction is "talks only to kube-apiserver" vs. "calls out to a specific cloud provider's API" — not about internet access, since both talk over the network.)

**Q7. Who handles pod-to-pod networking (not kube-proxy), and how?**
The **CNI plugin** (Calico, Cilium, Flannel, GKE VPC-native, etc.) — kubelet only *invokes* it once per pod (calls the CNI binary during sandbox creation), it doesn't do the networking itself. The CNI plugin assigns the pod an IP, creates a veth pair (one end in the pod netns as `eth0`, other end on a host bridge/route), and handles cross-node delivery via either an overlay (VXLAN encapsulation, e.g. Flannel), native routing/BGP (e.g. Calico BGP mode), or cloud-native VPC routing (GKE alias IPs — no encapsulation needed). kube-proxy is unrelated to this — it only does Service VIP → backend Pod IP translation via iptables/IPVS.

**Q8. Pod stuck in `Pending` — first suspect and first command?**
First suspect: **kube-scheduler** (or something it depends on) — `Pending` means the Pod exists in etcd but hasn't been bound to a node yet.
1. `kubectl get pod <name> -o wide` — check the `NODE` column. Empty → still unscheduled (scheduler's problem). Assigned but still Pending → shifts suspicion to kubelet/container runtime on that node instead.
2. `kubectl describe pod <name>` → check **Events** for `FailedScheduling`, e.g. `Insufficient cpu`, `didn't match node selector`, `node(s) had taints that the pod didn't tolerate`, or `volume node affinity conflict`.
3. If Events are unhelpful, check kube-scheduler's own logs (`kubectl logs -n kube-system <scheduler-pod>` on kubeadm, or the systemd journal on hard-way setups) for the scheduler loop itself erroring or not running.
