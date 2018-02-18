
## Containerizing a process for deployment

**In this section**, you will learn how to capture a simple node.js process in a docker container to run on the ICP platform. In addition you'll see how to wrap a docker image in a helm chart for deployment from the catalog.

Development processes such as these are typically sped up with enhancements such as automation DevOps processes, however this is a helpful to get a fundamental look at how some of the underlying parts of the process work.

## Task 1: Create a simple node.js process

In this section we'll create a simple node.js process and wrap it in a docker container. After testing that the container works locally as expected, we'll push the container to the  IBM Cloud Private registry and run it in our environment.


Create server.js using your preferred editor and add the following code:

```
  var http = require('http');

  var handleRequest = function(request, response) {
  console.log('Received request for URL: ' + request.url);
  response.writeHead(200);
  response.end('Hello World!');
  };
  var www = http.createServer(handleRequest);
  www.listen(8080);
```

Create Dockerfile and enter the following code

```
  FROM node:6.9.2
  EXPOSE 8080
  COPY server.js .
  CMD node server.js
```

First we'll establish a few environment variables

```
$ eval $(minikube docker-env)
```


Build the Docker image

```
$ docker build -t mynode:v1.0 .
Sending build context to Docker daemon  5.632kB
Step 1/4 : FROM node:6.9.2
6.9.2: Pulling from library/node
75a822cd7888: Pull complete
57de64c72267: Pull complete
4306be1e8943: Pull complete
871436ab7225: Pull complete
0110c26a367a: Pull complete
1f04fe713f1b: Pull complete
ac7c0b5fb553: Pull complete
Digest: sha256:2e95be60faf429d6c97d928c762cb36f1940f4456ce4bd33fbdc34de94a5e043
Status: Downloaded newer image for node:6.9.2
 ---> faaadb4aaf9b
Step 2/4 : EXPOSE 8080
 ---> Running in dbd5e8f531f1
 ---> 2c4ab49aacf4
Removing intermediate container dbd5e8f531f1
Step 3/4 : COPY server.js .
 ---> 5261850dc1f4
Removing intermediate container 30046a13c3e8
Step 4/4 : CMD node server.js
 ---> Running in 42c2917ec408
 ---> 187ba7937dd8
Removing intermediate container 42c2917ec408
Successfully built 187ba7937dd8
Successfully tagged mynode:v1.0
```

The container is built, and the docker client talking to the docker repository on the minikube image. Looking in the image repository we can see that both the base container as well as the container we've built are available in the repository.


```

$ docker images
REPOSITORY                                             TAG                 IMAGE ID            CREATED             SIZE
mynode                                                 v1.0                187ba7937dd8        4 minutes ago       655MB
gcr.io/google_containers/kubernetes-dashboard-amd64    v1.8.0              55dbc28356f2        2 months ago        119MB
gcr.io/k8s-minikube/storage-provisioner                v1.8.1              4689081edb10        3 months ago        80.8MB
gcr.io/google_containers/k8s-dns-sidecar-amd64         1.14.5              fed89e8b4248        4 months ago        41.8MB
gcr.io/google_containers/k8s-dns-kube-dns-amd64        1.14.5              512cd7425a73        4 months ago        49.4MB
gcr.io/google_containers/k8s-dns-dnsmasq-nanny-amd64   1.14.5              459944ce8cc4        4 months ago        41.4MB
gcr.io/google_containers/kubernetes-dashboard-amd64    v1.6.3              691a82db1ecd        6 months ago        139MB
gcr.io/google-containers/kube-addon-manager            v6.4-beta.2         0a951668696f        8 months ago        79.2MB
node                                                   6.9.2               faaadb4aaf9b        14 months ago       655MB
gcr.io/google_containers/pause-amd64                   3.0                 99e59f495ffa        21 months ago       747kB


```

From here, we can run the image on our kubernetes cluster.

```
$ kubectl run hello-node --image=mynode:v1.0 --port=8080
deployment "hello-node" created
$
$ kubectl get deployment
NAME         DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hello-node   1         1         1            1           29s
$
$ kubectl get pods
NAME                         READY     STATUS    RESTARTS   AGE
hello-node-77c96d485-qstmk   1/1       Running   0          3m

```

With the container running, we'll need to expose the applications port before we can access to application.


```
$ kubectl expose deployment hello-node --type=NodePort
service "hello-node" exposed
$ kubectl get services
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hello-node   NodePort    10.97.250.220   <none>        8080:32644/TCP   4s
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          5h

```

Now that the application is accessible via an external port, we're able to gain access to the services with curl

```  
$ kubectl get service
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
hello-node   NodePort    10.97.250.220   <none>        8080:32644/TCP   1m
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          5h

$ curl $(minikube service hello-node --url)
Hello World!

```
We've built and run our first container on Kubernetes!

---
