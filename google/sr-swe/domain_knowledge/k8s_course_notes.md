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

