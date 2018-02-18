


## Understanding Namespaces

**In this section**, we'll run our first container on Kubernetes.

Namespaces are about **isolation**...

- allowing different groups of people to share a cluster without having a collision of names.
- separating the same workloads for different purposes (DEV, TEST, PROD)
- establishing resource quotas to avoid "noisy neighbors"

Feel free to experiment with Namespaces along the way... you can create a namespace using object descriptions similarly to what we've already used.

Create a file named team-a.yaml and enter the following:

```
kind: Namespace
apiVersion: v1
metadata:
  name: team-a
  labels:
    name: team-a

```

Then create the namespace:
```
$ kubectl create -f team-a.yaml
namespace "team-a" created

```

Normally if you try to create 2 objects with the same name, there'll be a collision and the system will complain...

```
$ kubectl run nginx-name-collision --image=nginx --replicas=2
deployment "nginx-name-collision" created
$ kubectl run nginx-name-collision --image=nginx --replicas=2
Error from server (AlreadyExists): deployments.extensions "nginx-name-collision" already exists
```

Namespace isolation solves that problem by separating the workloads and avoiding collisions so users can share the cluster or even use different copies of the same workloads.

```
$ kubectl run nginx-name-collision --image=nginx --replicas=3 --namespace=team-a
deployment "nginx-name-collision" created
$
$ kubectl get deploy nginx-name-collision --namespace=default
NAME                   DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
nginx-name-collision   2         2         2            2           43s
irvingr@Richards-MacBook-Pro-2:~/Downloads/guestbook/namespace$ kubectl get deploy nginx-name-collision --namespace=team-a
NAME                   DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
nginx-name-collision   3         3         3            3           27s

```

Give it a try! - create a namespace (or 2, or 3) and recreate some of the deployments we've tried in a namespace and see what happens... 



---
