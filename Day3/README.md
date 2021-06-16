
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
The expected output is shown below
<pre>
[jegan@localhost centos-ansible]$ docker images
REPOSITORY                     TAG            IMAGE ID       CREATED          SIZE
tektutor/ansible-node-centos   latest         3439a96e8dd7   13 minutes ago   250MB
tektutor/ansible-node-ubuntu   latest         98001440d32d   23 minutes ago   220MB
tektutor/maven                 2.0            f81e2e72206f   25 hours ago     283MB
tektutor/maven                 1.0            727fddfe8301   25 hours ago     560MB
wordpress                      latest         c2dd1984ad5b   12 days ago      551MB
nginx                          1.20           993ef3592f66   3 weeks ago      133MB
ubuntu                         16.04          9ff95a467e45   3 weeks ago      135MB
ubuntu                         18.04          81bcf752ac3d   3 weeks ago      63.1MB
mysql                          latest         c0cdc95609f1   4 weeks ago      556MB
alpine                         latest         6dbb9cc54074   2 months ago     5.61MB
centos                         8              300e315adb2f   6 months ago     209MB
openjdk                        8-jdk-alpine   a3562aa0b991   2 years ago      105MB
[jegan@localhost centos-ansible]$ 
</pre>

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
The expected output is shown below
<pre>
[jegan@localhost centos-ansible]$ docker ps
CONTAINER ID   IMAGE                                 COMMAND               CREATED          STATUS          PORTS                                                                          NAMES
7e4d898ee3d1   tektutor/ansible-node-centos:latest   "/usr/sbin/sshd -D"   2 seconds ago    Up 1 second     0.0.0.0:2004->22/tcp, :::2004->22/tcp, 0.0.0.0:8004->80/tcp, :::8004->80/tcp   centos2
2209b75db03f   tektutor/ansible-node-centos:latest   "/usr/sbin/sshd -D"   15 seconds ago   Up 13 seconds   0.0.0.0:2003->22/tcp, :::2003->22/tcp, 0.0.0.0:8003->80/tcp, :::8003->80/tcp   centos1
c25d3ef37440   tektutor/ansible-node-ubuntu:latest   "/usr/sbin/sshd -D"   37 seconds ago   Up 35 seconds   0.0.0.0:2002->22/tcp, :::2002->22/tcp, 0.0.0.0:8002->80/tcp, :::8002->80/tcp   ubuntu2
089668131eb7   tektutor/ansible-node-ubuntu:latest   "/usr/sbin/sshd -D"   49 seconds ago   Up 48 seconds   0.0.0.0:2001->22/tcp, :::2001->22/tcp, 0.0.0.0:8001->80/tcp, :::8001->80/tcp   ubuntu1
[jegan@localhost centos-ansible]$ 
</pre>

