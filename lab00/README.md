

### Creating a Working Environment
In this section we'll install the tools required to run containers locally on the docker engine, as well as on minikube to better see container orchestration in action. If you already have a working Minikube installation you can skip this section.

We'll need to install Minkube as a runtime environment as well as the kubectl client and the Docker engine.  

**Installing the Docker engine**

Technically... you don't need docker installed because minikube already has it available... however we'll, take a brief look at docker and run a few containers before we try out kubernetes, so docker engine will need to be installed.

If you're [hearing about Docker for the first time](https://www.docker.com/what-container), Dockers website is a great place to get context.

The getting started guide on Docker has detailed instructions for installing Docker for [Mac](https://www.docker.com/community-edition#/mac), [Windows](https://www.docker.com/community-edition#/windows)

When Docker is installed, it can be easily tested by running the "hello-world" container:
```
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
ca4f61b1923c: Pull complete
Digest: sha256:66ef312bbac49c39a89aa9bcc3cb4f3c9e7de3788c944158df3ee0176d32b751
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.
...

```
---


**Installing Virtualbox**
For these labs, we'll need Virtualbox installed. Minikube actually downloads a virtual machine that it runs in virtualbox, which makes the environment easy to manage.

If you don't have Virtualbox already installed, you can find the [binaries](https://www.virtualbox.org/wiki/Downloads) for your platform to get a current version of Virtualbox installed. The labs were tested on Virtualbox v5.1.30 though the version you have installed may be different.

```
$ vboxmanage --version
5.1.30r118389

$ VBoxManage list vms
"minikube" {298b5694-d780-4e88-a351-e94b8635e22d}

```

---

**Installing Minikube**

Minikube makes it easy to run an easy to use, installation of Kubernetes that's great to run locally for development, testing, and learning how Kubernetes works.  Minikube runs a single-node Kubernetes cluster inside a VM on your laptop for users looking to try out Kubernetes or develop with it day-to-day. You have the option of using one of several hypervisors, but we'll let Minikube use Virtualbox.

For this tutorial we'll download minikube v0.24.1. Binaries are available for [Mac](https://storage.googleapis.com/minikube/releases/v0.24.1/minikube-darwin-amd64), [Linux](https://storage.googleapis.com/minikube/releases/v0.24.1/minikube-linux-amd64), [Windows](https://storage.googleapis.com/minikube/releases/v0.24.1/minikube-windows-amd64.exe)

Starting Minikube for the first time, it will download the iso image it needs to start the Kubernetes cluster

```

$ minikube start
There is a newer version of minikube available (v0.25.0).  Download it here:
https://github.com/kubernetes/minikube/releases/tag/v0.25.0

To disable this notification, run the following:
minikube config set WantUpdateNotification false
Starting local Kubernetes v1.8.0 cluster...
Starting VM...
Downloading Minikube ISO
 140.01 MB / 140.01 MB [============================================] 100.00% 0s
Getting VM IP address...
Moving files into cluster...
Downloading localkube binary
 148.25 MB / 148.25 MB [============================================] 100.00% 0s
 0 B / 65 B [----------------------------------------------------------]   0.00%
 65 B / 65 B [======================================================] 100.00% 0sSetting up certs...
Connecting to cluster...
Setting up kubeconfig...
Starting cluster components...
Kubectl is now configured to use the cluster.
Loading cached images from config file.


```
We'll also [install the kubectl client](https://kubernetes.io/docs/tasks/tools/install-minikube/)... for this tutorial we'll install kubectl v1.8.8... download either the [Mac](https://dl.k8s.io/v1.8.8/kubernetes-client-darwin-amd64.tar.gz), [Linux](https://dl.k8s.io/v1.8.8/kubernetes-client-linux-amd64.tar.gz) or [Windows](https://dl.k8s.io/v1.8.8/kubernetes-client-windows-amd64.tar.gz) binaries appropriate for your system and make sure its available in your path.

Next, lets check that kubectl is properly configured by getting the cluster state:
```
$ kubectl cluster-info
Kubernetes master is running at https://192.168.99.100:8443

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.

```


---
