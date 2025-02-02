


## Deploying a Container to Kubernetes

**In this section**, we'll run our first container on Kubernetes.

## Task 1: Deploy an Nginx server

In this section we'll deploy an nginx server to our minikube cluster.... 

```
$  kubectl create deploy nginx --image nginx:1.25 --replicas 3
deployment.apps/nginx created

$  kubectl get deploy
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   3/3     3            3           46s
$
$  kubectl get pods
NAME                     READY   STATUS    RESTARTS   AGE
nginx-8ff954c69-4v5c9   1/1     Running   0          23s
nginx-8ff954c69-kg8r4   1/1     Running   0          23s
nginx-8ff954c69-pkc8h   1/1     Running   0          23s

```

Now we have a container running...we'll need to provide access to the server by creating a [service](https://kubernetes.io/docs/concepts/services-networking/service/) to make a port available.


```
$ kubectl expose deploy nginx --port 80 --type=NodePort

$ kubectl get service
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP        58m
nginx        NodePort    10.99.227.117   <none>        80:30870/TCP   5s

```

The port is open, so the nginx server should be available... keep in mind, however, that the kubernetes environment is running in the minikube vm, so we'll have to use its ip to access the server. Fortunately there's an easy way to identify the proper ip:

```
$  minikube service nginx --url
http://127.0.0.1:59364
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
$
$ curl http://127.0.0.1:59364
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
.
.
.
</html>
```

## Task 2: Scale the Nginx deployment and test its resilience

The server is deployed, but what if we got a lot more traffic than we expected? Fortunately we have the option to easily update our deployments to account for scalability and updates to our applications.

If we needed to scale our deployment to have more servers, we can use kubectl to do that as well...lets scale our deployment so it has a total of 5 pods.

```
$ kubectl scale deploy nginx --replicas=5
deployment.apps/nginx scaled
$
$ kubectl get pods
NAME                    READY   STATUS    RESTARTS   AGE
nginx-8ff954c69-4v5c9   1/1     Running   0          101s
nginx-8ff954c69-4wqmc   1/1     Running   0          4s
nginx-8ff954c69-kg8r4   1/1     Running   0          101s
nginx-8ff954c69-pkc8h   1/1     Running   0          101s
nginx-8ff954c69-s9htq   1/1     Running   0          4s
```

Our workloads on Kubernetes are quite resilient if we let the system handle things for us. When we asked the system to scale our Nginx deployment, it created a replicaset. A ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides a lot of other useful features.

Let's see how resilient our workload is by deleting a few pods!

```
$ kubectl  delete pods nginx-8ff954c69-s9htq nginx-8ff954c69-4v5c9
pod "nginx-8ff954c69-s9htq" deleted
pod "nginx-8ff954c69-4v5c9" deleted

```
The pods are deleted as requested... but for both deleted pods, a new pod has been created in its place! Best of all... the service continues to keep track of all the appropriate pods and route traffic to them as soon as they're available.

```
$ kubectl  get pods
NAME                    READY   STATUS              RESTARTS   AGE
nginx-8ff954c69-4wqmc   1/1     Running             0          56s
nginx-8ff954c69-c6wv5   0/1     ContainerCreating   0          2s
nginx-8ff954c69-kg8r4   1/1     Running             0          2m33s
nginx-8ff954c69-mblkd   0/1     ContainerCreating   0          2s
nginx-8ff954c69-pkc8h   1/1     Running             0          2m33s
```


## Task 3: Update the pod with a new version of the software

It's great that the system is deployed, running, and scaling... but what happens when we have new versions of our software to deploy? To do that we can simply update the existing deployment and tell it that there's a new version to roll out.

```
$ kubectl set image deployment/nginx nginx=nginx:1.27
deployment.apps/nginx image updated

```

When we tell kubernetes that our deployment needs to update a new container image it coordinates with the service to terminate the old versions, roll out the new versions and ensure that the service continues to route traffic to the proper pods.

```

$ kubectl get pods
NAME                     READY   STATUS              RESTARTS   AGE
nginx-5fdc696c4c-84s9g   0/1     ContainerCreating   0          6s
nginx-5fdc696c4c-hhd4s   0/1     ContainerCreating   0          6s
nginx-5fdc696c4c-tb7q4   0/1     ContainerCreating   0          6s
nginx-8ff954c69-4wqmc    1/1     Running             0          99s
nginx-8ff954c69-kg8r4    1/1     Running             0          3m16s
nginx-8ff954c69-mblkd    1/1     Running             0          45s
nginx-8ff954c69-pkc8h    1/1     Running             0          3m16s

```

To validate that the proper pod is running, do a 'describe' on the deployment or one of the pods and see what image is currently in use...

Now that we've gotten a bit of a feel for working with Kubernetes we can clean up and move on to the next thing!

```
$ kubectl delete deployment nginx
deployment.apps "nginx" deleted

$ kubectl delete service nginx
service "nginx" deleted
```

---
