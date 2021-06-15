## Setting the Lab environment

### Installing Docker Community Edition
```
sudo yum install -y yum-utils
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce
```

### Start the docker service
```
sudo systemctl enable docker
sudo systemctl start docker
```
