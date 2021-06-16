
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
cp /home/jegan/.ssh/id_rsa.pub authorized_keys
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
cp /home/jegan/.ssh/id_rsa.pub authorized_keys
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
