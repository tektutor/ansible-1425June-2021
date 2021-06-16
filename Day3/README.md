
## Ansible Overview

### Ansible Commands

#### Ansible version
```
ansible --version
```
#### Generating ssh key pair
Assumption is you are generating key for non-admin user.
```
ssh-keygen
```
Hit Enter key 3 times to accept all defaults.

#### Building custom ansible node ubuntu docker image
```
cd Day3/ubuntu-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-node-ubuntu .
```
#### Check if the images is build successfully
```
docker images
```
If the image was successfuly build, you will see an image with name "tektutor/ansible-node-ubuntu:latest"

#### Building custom ansible node centos docker image
```
cd Day3/centos-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
docker build -t tektutor/ansible-node-centos .
```
#### Check if the images is build successfully
```
docker images
```
If the image was successfuly build, you will see an image with name "tektutor/ansible-node-centos:latest"

#### Clean up existing containers
```
docker rm -f $(docker ps -aq)
```

#### Create container from the custom docker images
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ansible-node-ubuntu:latest
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ansible-node-ubuntu:latest

docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/ansible-node-centos:latest
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/ansible-node-centos:latest
```

#### Check if all the 4 containers are running
```
docker ps
```
The expected output is similar to this
<pre>
[jegan@localhost centos-ansible]$ docker ps
CONTAINER ID   IMAGE                                 COMMAND               CREATED          STATUS          PORTS                                                                          NAMES
7e4d898ee3d1   tektutor/ansible-node-centos:latest   "/usr/sbin/sshd -D"   2 seconds ago    Up 1 second     0.0.0.0:2004->22/tcp, :::2004->22/tcp, 0.0.0.0:8004->80/tcp, :::8004->80/tcp   centos2
2209b75db03f   tektutor/ansible-node-centos:latest   "/usr/sbin/sshd -D"   15 seconds ago   Up 13 seconds   0.0.0.0:2003->22/tcp, :::2003->22/tcp, 0.0.0.0:8003->80/tcp, :::8003->80/tcp   centos1
c25d3ef37440   tektutor/ansible-node-ubuntu:latest   "/usr/sbin/sshd -D"   37 seconds ago   Up 35 seconds   0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
089668131eb7   tektutor/ansible-node-ubuntu:latest   "/usr/sbin/sshd -D"   49 seconds ago   Up 48 seconds   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1
[jegan@localhost centos-ansible]$ 
</pre>

