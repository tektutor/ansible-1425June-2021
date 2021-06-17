### Make sure your containers are in running state
```
docker ps
```

### In case your container are in Exited state, you may see them with below command
```
docker ps -a
```

### In case they are Exited, you need to start them
```
docker start $(docker ps -aq)
```

### Running the ping playbook
```
ansible-playbook -i inventory ping.yml
```

### Running the install vim playbook
```
ansible-playbook -i inventory install-vim.yml
```

### Running the install vim playbook with verbosity enabled
```
ansible-playbook -i inventory install-vim.yml -vvvv
```

### Running the install nginx playbook
```
ansible-playbook -i inventory install-nginx-playbook.yml
```
