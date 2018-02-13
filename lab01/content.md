

## Running our first container...

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
