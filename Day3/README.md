
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
