


## Deploying a Container to Kubernetes

**In this section**, we'll run our first container on Kubernetes.

There's a rich command line api for running containers, but this time we'll do it a little differently... we'll create a file to desribe the Kubernetes Objects we're going to create. That makes it convenient to capture what we want deployed, and how.

Development processes such as these are typically sped up with enhancements such as automation DevOps processes, however this is a helpful to get a fundamental look at how some of the underlying parts of the process work.

## Task 1: Deploy an Nginx server

In this section we'll deploy an nginx server.... lets start by running a container


```
$ kubectl run my-deploy --image=nginx:1.7.9 --port=80
deployment "my-deploy" created
$
$ kubectl get deploy
NAME        DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
my-deploy   1         1         1            1           1m
$
$ kubectl get pods
NAME                         READY     STATUS        RESTARTS   AGE
my-deploy-dbc4b8b5d-krhwh    1/1       Running       0          1m

```

Now we have a container running...we'll need to provide access to the server by creating a [service](https://kubernetes.io/docs/concepts/services-networking/service/) to make a port available.


```
$ kubectl expose deployment my-deploy  --type=LoadBalancer
service "my-deploy" exposed
$
$ kubectl get service
NAME         TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP          1d
my-deploy    LoadBalancer   10.111.227.3    <pending>     80:30839/TCP     1m


```

The port is open, so the nginx server should be available... keep in mind, however, that the kubernetes environment is running in the minikube vm, so we'll have to use its ip to access the server. Fortunately there's an easy way to identify the proper ip:

```
$ minikube ip
192.168.99.100

```
Then we can assemble the url... as http:// + [minikube ip] + ":" + [port assigned by minikube service].
If we put it all together, based on what's listed above: http://192.168.99.100:30839

```
$ curl http://192.168.99.100:30839
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>

...
</html>
```

An alternative is to use minikube's 'service' sub-command which makes it easier to get the required url.

```
$ curl $(minikube service my-deploy --url)
```

## Task 2: Scale the Nginx deployment and test its resilience

The server is deployed, but what if we got a lot more traffic than we expected? Fortunately we have the option to easily update our deployments to account for scalability and updates to our applications.

If we needed to scale our deployment to have more servers, we can use kubectl to do that as well...lets scale our deployment so it has a total of 5 pods.

```
$ kubectl scale deploy my-deploy --replicas=5
deployment "my-deploy" scaled
$
$ kubectl get deploy
NAME        DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
my-deploy   5         5         5            5           58s
$
$ kubectl get pods
NAME                         READY     STATUS    RESTARTS   AGE
my-deploy-6fd857889c-8pm6x   1/1       Running   0          50s
my-deploy-6fd857889c-ht7pv   1/1       Running   0          1m
my-deploy-6fd857889c-kkx5k   1/1       Running   0          50s
my-deploy-6fd857889c-nmccq   1/1       Running   0          50s
my-deploy-6fd857889c-xqvqz   1/1       Running   0          50s

```

Our workloads on Kubernetes are quite resilient if we let the system handle things for us. When we asked the system to scale our Nginx deployment, it created a replicaset. A ReplicaSet ensures that a specified number of pod replicas are running at any given time. However, a Deployment is a higher-level concept that manages ReplicaSets and provides a lot of other useful features.

Let's see how resilient our workload is by deleting a few pods!

```
$ kubectl delete pod my-deploy-6fd857889c-xqvqz my-deploy-6fd857889c-nmccq
pod "my-deploy-6fd857889c-xqvqz" deleted
pod "my-deploy-6fd857889c-nmccq" deleted


```
The pods are deleted as requested... but for both deleted pods, a new pod has been created in its place! Best of all... the service continues to keep track of all the appropriate pods and route traffic to them as soon as they're available.

```
$ kubectl get pods
NAME                         READY     STATUS        RESTARTS   AGE
my-deploy-6fd857889c-8nvf5   1/1       Running       0          12s
my-deploy-6fd857889c-8pm6x   1/1       Running       0          3m
my-deploy-6fd857889c-dzwlf   1/1       Running       0          12s
my-deploy-6fd857889c-ht7pv   1/1       Running       0          4m
my-deploy-6fd857889c-kkx5k   1/1       Running       0          3m
my-deploy-6fd857889c-nmccq   0/1       Terminating   0          3m
my-deploy-6fd857889c-xqvqz   0/1       Terminating   0          3m
```


## Task 3: Update the pod with a new version of the software

It's great that the system is deployed, running, and scaling... but what happens when we have new versions of our software to deploy? To do that we can simply update the existing deployment and tell it that there's a new version to roll out.

```
$ kubectl set image deployment/my-deploy my-deploy=nginx:1.9
deployment "my-deploy" image updated

```

When we tell kubernetes that our deployment needs to update a new container image it coordinates with the service to terminate the old versions, roll out the new versions and ensure that the service continues to route traffic to the proper pods.

```

$ kubectl get pods
NAME                         READY     STATUS        RESTARTS   AGE
my-deploy-6fd857889c-8nvf5   0/1       Terminating   0          17m
my-deploy-6fd857889c-8pm6x   0/1       Terminating   0          20m
my-deploy-6fd857889c-dzwlf   0/1       Terminating   0          17m
my-deploy-6fd857889c-ht7pv   0/1       Terminating   0          21m
my-deploy-6fd857889c-kkx5k   0/1       Terminating   0          20m
my-deploy-857bc7b484-4j684   1/1       Running       0          11s
my-deploy-857bc7b484-mx75q   1/1       Running       0          12s
my-deploy-857bc7b484-phfct   1/1       Running       0          10s
my-deploy-857bc7b484-ttspq   1/1       Running       0          13s
my-deploy-857bc7b484-w27c2   1/1       Running       0          13s

```

To validate that the proper pod is running, do a 'describe' on the deployment or one of the pods and see what image is currently in use...

Now that we've gotten a bit of a feel for working with Kubernetes we can clean up and move on to the next thing!

```
$ kubectl delete deployment my-deploy
deployment "my-deploy" deleted

```



---
