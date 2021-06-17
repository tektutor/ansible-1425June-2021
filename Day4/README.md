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

### Check if you are able to access the custom web page from 'ubuntu1', 'ubuntu2', 'centos1' and 'centos2' ansible nodes respectively
```
curl http://localhost:8001
curl http://localhost:8002
curl http://localhost:8003
curl http://localhost:8004
```
Notice, the hostname variable gives different values depending on the ansible node.

### Ansible Configuration File
Ansible looks for ansible.cfg file in the local directory, if not found then it attempts to locate the .ansible.cfg under your home directory and if not found there too it make a final attempt to locate at /etc/ansible/ansible.cfg.  Wherever ansible finds the configuration file first, it picks it from the there.

A simple ansible.cfg file looks as shown below
```
[defaults]
deprecation_warnings=False
inventory=./inventory
```
If ansible.cfg file points to your inventory, then you may execute the ad-hoc and playbooks as shown below
```
ansible all -m ping
ansible centos1 -m ping
ansible-playbook install-vim.yml
```

### Limitting the playbook execution to a spectific group or a particular machine without modifying playbook
```
ansible-playbook install-nginx-playbook.yml --limit qa
ansible-playbook install-nginx-playbook.yml --limit centos1
```
