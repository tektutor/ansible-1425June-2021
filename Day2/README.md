### Port Forwarding
```
docker run -d --name nginx1 --hostname nginx1 -p 8001:80 nginx:1.20 
```

### Accessing nginx web page
```
curl http://localhost:8001
```

### Accessing nginx web page from web browser
```
http://localhost:8001
```

### Volume Mounting
```
docker run -d --name mysql1 --hostname mysql1 -v /tmp/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:latest
```

## Wordpress with MySQL
This demonstrates how a multi-container application is deployed in docker.

### Cleanup existing containers
```
docker rm -f $(docker ps -aq)
```

### Create the MySQL container
```
docker run -d --name mysql1 --hostname mysql1 -e MYSQL_ROOT_PASSWORD=root mysql:8.0 
```

### Create Wordpress database
```
docker exec -it mysql1 sh
mysql -u root -p
CREATE DATABASE wordpress;
```
When prompts for password, type 'root' as the password.

### Find the IP Address of mysql1 container
```
docker inspect mysql1 | grep IPA

docker inspect -f {{.NetworkSettings.IPAddress}} mysql1
```
Assuming the mysql1 container IP address is 172.17.0.3

### Create the wordpress
```
docker run --name wordpress1 -e WORDPRESS_DB_HOST=172.17.0.3:3306 \
    -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=root -d wordpress
```

### Find the IP Address of the wordpress1 container
```
docker inspect wordpress1 | grep IPA
```

### Access the wordpress web page from Lab machine web browser
The assumption is 172.17.0.2 is the IP Address of wordpress1 container.
```
http://172.17.0.2:80
```

### Clean up all containers
```
docker rm -f $(docker ps -aq)
```

### List the docker networks
```
docker network ls
```

### Docker default network
Docker uses 'docker0' bridge network as the default network.  If a container is created and not connected to a custom-network, they 
are by default connected to 'docker0' bridge network.  The 'docker0' is a software defined bridge network.  The subnet IP address assigned to this network is 172.17.0.0/16.  Technically, 65535 containers can be part of this network. However, some IP addresses are reserved for docker's internal use, for example 172.17.0.1 is used for GateWay.  It is through the Gateway containers will be able to communicate to outside world or internet.

### Create ubuntu1 and ubuntu2 containers
```
docker run -dit --name ubuntu1 --hostname ubuntu1 ubuntu:16.04 /bin/bash
docker run -dit --name ubuntu2 --hostname ubuntu2 ubuntu:16.04 /bin/bash
```

### Inspect container ubuntu1
```
docker inspect ubuntu1 | grep IPA
```
You may notice that the IP Address of ubuntu1 is 172.17.0.2 

### Inspect container ubuntu2
```
docker inspect ubuntu1 | grep IPA
```
YOu may notice that the IP Address of ubuntu2 is 172.17.0.3

### Inspect bridge network
```
docker network inspect bridge
```
You can observe now that ubuntu1 and ubuntu2 are added to default 'bridge' network and acquired an IP from the bridge network subnet (172.17.0.0/16).

### Containers from same network can access each other by default

### Connect to ubuntu1 
```
docker exec -it ubuntu1 bash
apt update && apt install -y iputils-ping net-tools
```

### From another tab connect to ubuntu2
```
docker exec -it ubuntu2 bash
apt update && apt install -y iputils-ping net-tools
```

### Try pinging ubuntu2 from ubuntu1 container
```
ping 172.17.0.3
```
You would have observed practically that ubuntu1 is able to reach to ubuntu2. The reason is they are in the same network.

### Try pinging ubuntu1 from ubuntu2 container
```
ping 172.17.0.2
```
You would have observed practically that ubuntu2 is able to reach to ubuntu1.  The reason is they are in the same network.

### Remove existing containers
```
docker rm -f $(docker ps -aq)
```

### Create your custom network
```
docker network create my-network-1
docker network create my-network-2
```

### Inspect the Subnet address assigned to my-network-1
```
docker network inspect my-network-1
```
You would have noticed that my-network-1 is assigned with 172.18.0.0/16 subnet address.

### Inspect the Subnet address assigned to my-network-2
```
docker network inspect my-network-2
```
You would have noticed that my-network-2 is assigned with 172.19.0.0/16 subnet address.


### You could also create a custom network with a custom subnet address
```
docker network create test-network --subnet 192.168.0.0/16
```

### You may inspect test-network to verify the subnet IP address range
```
docker network inspect test-network
```
You would noticed that test-network is assinged with a custom subnet ip range 192.168.0.0/16.  Assumption is 192.168.0.0/16 is not already taken by other networks on your system.

### Deleting a custom network
```
docker network rm test-network
```
