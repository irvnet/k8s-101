
## Getting familiar with Kubernetes

In this section, lets get familiar with kubernetes by looking around the environment.

A local, single node installation of a Kubernetes cluster is great for our purpose, which is to learn more about how Kubernetes works without getting to distracted by the details of setting up a multi-node cluster.

![](../images/minikube-installation.jpg)

Now we're ready to take a closer look at minikube. Typing "minikube" at the prompt returns the usage statement. First we'll start minikube to get our cluster up and running.

```
$ minikube start
😄  minikube v1.35.0 on Darwin 15.3
✨  Automatically selected the docker driver. Other choices: virtualbox, ssh
📌  Using Docker Desktop driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🔥  Creating docker container (CPUs=2, Memory=4000MB) ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

```

Now that our cluster is up and running, we can explore a little... lets start by checking the status of our cluster.

```
$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

```

Between minikube and kubectl we can look around at our environment. Run 'minikube' and 'kubectl' and take a look at the usage statement to see what the key commands are.

Now, lets interrogate the cluster... though a kubernetes cluster likely has multiple nodes, minikube is a single node cluster that's helpful for development and testing.

```
$ kubectl get nodes
NAME       STATUS   ROLES           AGE     VERSION
minikube   Ready    control-plane   3h37m   v1.32.0


```

We can check if there's a more updated version of minikube:

```
$ minikube update-check
CurrentVersion: v1.35.0
LatestVersion: v1.35.0
```

We can also see what pods are running using kubectl. We haven't run any pods yet, but there are some system pods we can take a look at...

```
$ kubectl get pods --all-namespaces
NAMESPACE     NAME                               READY   STATUS    RESTARTS      AGE
kube-system   coredns-668d6bf9bc-8prvr           1/1     Running   0             70s
kube-system   etcd-minikube                      1/1     Running   0             75s
kube-system   kube-apiserver-minikube            1/1     Running   0             76s
kube-system   kube-controller-manager-minikube   1/1     Running   0             75s
kube-system   kube-proxy-6mkks                   1/1     Running   0             70s
kube-system   kube-scheduler-minikube            1/1     Running   0             76s
kube-system   storage-provisioner                1/1     Running   1 (40s ago)   73s

```
---
