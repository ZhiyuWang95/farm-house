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
