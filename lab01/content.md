
## Containerizing a process for deployment

**In this section**, we'll create a few containers and run them locally. We'll see the basics of running a container as well as learn how to capture a simple node.js process in a docker container and run it locally using the Docker engine.

Development processes such as these are typically sped up with enhancements such as automation DevOps processes, however this is a helpful to get a fundamental look at how some of the underlying parts of the process work.

## Task 1: Running our first container...

In this section we'll run a container and see how the mechanism works.

Now that we have everything working its time to see more closely how to run containers. In this section, we'll run an Ubuntu 16.04 container to see how things work.

At the terminal enter:

```

$docker pull ubuntu:16.04

```

This brings the ubuntu container to our local machine and stores it in the docker repository. From there you can see a list of all the containers in the local repository.

```

$docker images

```

Now we can run the ubuntu container

```
$ docker run -it --name myFirstContainer ubuntu /bin/bash
root@d9389be0b795:/#
root@d9389be0b795:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@d9389be0b795:/#
root@d9389be0b795:/#
root@d9389be0b795:/# exit
exit
$

```

We can see the list of containers that are running, or that have exited

```
$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
d9389be0b795        ubuntu              "/bin/bash"         4 minutes ago       Exited (0) 2 minutes ago                       myFirstContainer
```

... and we can remove any containers that are no longer in use

```
$ docker rm myFirstContainer
myFirstContainer

```

Congratulations! - you've run your first container!

---


## Task 2: Create a simple node.js process

In this section we'll create a simple node.js process and wrap it in a docker container. 


1. create server.js using your preferred editor and add the following code:
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

2. Create Dockerfile and enter the following code

```
  FROM node:6.9.2
  EXPOSE 8080
  COPY server.js .
  CMD node server.js
```

3. Build the Docker image
```
$ docker build -t mynode:v1.0 .
```

4. Run the image and test it locally

```
$ docker run --rm -d -p 8080:8080 --name mynode-sample  hello-node:v1
```

  For a quick test of the container running locally on your machine, In your browser, access http://localhost:8080.  

5. Stop the locally running container

```  
$ docker stop mynode-sample
```


---
