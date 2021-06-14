## Setting the Lab environment
The assumption is that you already have a CentOS 8.3.x 64-bit OS.

### Installing Docker Community Edition
```
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
```

## Managing Docker Images

### Start the docker service
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker jegan
```
You may have to replace the user 'jegan' with your username.

### Listing the docker images in local registry
```
docker images
```

### Download a docker image from Docker Hub to Local Docker Registry
```
docker pull hello-world:latest
docker pull ubuntu:16.04
```

### Deleting a docker image
```
docker rmi hello-world:latest

```

### Finding more details about the image
```
docker image inspect ubuntu:16.04
```

## Managing Docker Containers

### Creating a container in background(deattchaed/daemon) mode
```
docker run --dit --name ubutu2 --hostname ubuntu2 ubuntu:16.04 /bin/bash
```

### Creating a container in interactive mode
```
docker run hello-world:latest
docker run --it --name ubuntu1 --hostname ubuntu1 ubuntu:16.04 /bin/bash
```

### Listing the currenly running containers
```
docker ps
```


### Listing all containers
```
docker ps -a
```

### Listing containers with a specific name pattern
```
docker ps --filter="name=ubuntu"
docker ps --filter="name=ubu"
```

### Deleting containers matching  a spectific name pattern
```
docker rm -f $(docker ps -q --filter="name=ubuntu") 
```

### Finding IP Address of a container
```
docker inspect ubuntu1 | grep IPA
docker inspect -f {{.NetworkSettings.IPAddress}} ubuntu1
```

### Stopping a running container
```
docker stop ubuntu1
```

### Starting a stopped container
```
docker start ubuntu1
```

### Docker rename container
```
docker rename old-container-name new-container-name
```

### Restarting a container
```
docker restart ubuntu1
```

### Getting inside a running container
```
docker exec -it ubuntu1 /bin/bash
```

### Coming out of container
```
exit
```

### Deleting a container graciously
```
docker stop ubuntu1
docker rm ubuntu1
docker stop ubuntu2 && docker rm ubuntu2
docker stop ubuntu1 ubuntu2 ubuntu3
docker rm ubuntu1 ubuntu2 ubuntu3
docker stop $(docker ps -q) && docker rm $(docker ps -aq)
```

### Deleting a container forcibly
```
docker rm -f ubuntu1
docker rm -f $(docker ps -aq)
```
