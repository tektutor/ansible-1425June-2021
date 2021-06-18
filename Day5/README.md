### Running the playbook
By default the existing containers will not be deleted
```
ansible-playbook provision-docker-containers.yml
```

If you wish to delete the existing containers, you may do so as shown below
```
ansible-playbook provision-docker-containers.yml -e delete_containers=yes
```

### Passing multiple extra variables to playbook from CLI
```
ansible-playbook provision-docker-containers.yml -e delete_containers=yes -e second_var=1
ansible-playbook provision-docker-containers.yml -e "delete_container=yes second_var=1"
```
