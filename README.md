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

### Start the docker service
```
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker jegan
```
You may have to replace the user 'jegan' with your username.
