

## Running our first container...

In this section we'll run a container with the Ubuntu operating system and see how the mechanism works.

At the terminal enter:
```

$docker pull ubuntu:22.04
22.04: Pulling from library/ubuntu
6414378b6477: Pull complete
Digest: sha256:0e5e4a57c2499249aafc3b40fcd541e9a456aab7296681a3994d631587203f97
Status: Downloaded newer image for ubuntu:22.04
docker.io/library/ubuntu:22.04
```
This brings the ubuntu container to our local machine and stores it in the image repository. From there you can see a list of all the locally available images.

```

$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    74cc54e27dc4   10 days ago    10.1kB
ubuntu        22.04     97271d29cb79   4 months ago   77.9MB
```

Now we can use the local image to create a running instance of a container with the Ubuntu operating system:

```

 docker run -it --name myFirstContainer ubuntu:22.04 /bin/bash
root@cb09f1167ce2:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@cb09f1167ce2:/# exit
exit
$
```

We can see the list of containers that are running, or that have exited

```

$ docker ps -a
CONTAINER ID   IMAGE          COMMAND       CREATED          STATUS                     PORTS     NAMES
1b7bca777fbd   ubuntu:22.04   "/bin/bash"   10 seconds ago   Exited (0) 5 seconds ago             myFirstContainer
```

... and we can remove any containers that are no longer in use

```

$ docker rm myFirstContainer
myFirstContainer

```

Congratulations! - you've run your first container!

---
