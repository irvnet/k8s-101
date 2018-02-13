
**Session Objective:**  introduction to containers and Kubernetes. Overview of the "what" and "why" of Docker containers and an overview of container orchestration with Kubernetes. In addition to lecture and discussion will be some hands on labs to demonstrate how to install the required tools and see how containers work in practice. Attending this session will give you the basic skills to explore and experiment with containers to determine how they best fit your use cases, or just to have fun with them!

**Proposed Duration**: 2hrs including ~30 minutes of presentation and ~90 minutes of hands on exercises

---

### Agenda Overview

**Presentation and Discussion**

- What are containers (lxc/d -> docker -> Borg -> K8s)?
- Containers or virtual machines? (smaller, lighter, faster, but... more like containers AND vm's till you technical debt is paid...)
- What is "container orchestration" and what does [Kubernetes](https://kubernetes.io/) do?
- Why does this matter for businesses? -  ease of use, stability, scalability

**10 minute break**

**Understanding Docker**

- [lab 00](lab00/content.md): creating a working environment - installing virtualbox, docker, minikube and kubectl on the local machine
- [lab 01](lab01/content.md): first container - pull, run, review, stop an nginx container
- [lab 02](lab02/content.md): creating your first container - creating and running your first container with a dockerfile and a node.js process

**Getting Started with Minikube** 

- [lab 03](lab03/content.md): starting minikube - minikube start, kubectl cluster-info, kubectl get-nodes, minkube dashboard
- [lab 04](lab04/content.md): deploy a web server - kubectl run, kubectl expose deployment, curl

**Deploying an application on minikube**

- [lab 05](lab05/content.md): Containerize and deploy a node.js process
- [lab 06](lab06/content.md): deploying the Guestbook Application

**Discussion and Questions**

---
