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

### Cleanup existing containers
```
docker rm -f $(docker ps -aq)
```

### Create the MySQL container
```
docker run -d --name mysql1 --hostname mysql1 -e MYSQL_ROOT_PASSWORD=root mysql:8.0 
```

### Find the IP Address of mysql1 container
```
docker inspect mysql1 | grep IPA

docker inspect -f {{.NetworkSettings.IPAddress}} mysql1
```

### Create the wordpress
```
docker run --name some-wordpress -e WORDPRESS_DB_HOST=172.17.0.3:3306 \
    -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=root -d wordpress
```
