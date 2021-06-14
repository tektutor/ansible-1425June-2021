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

## Managing Docker Containers

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

### Restarting a container
```
docker restart ubuntu1
```
