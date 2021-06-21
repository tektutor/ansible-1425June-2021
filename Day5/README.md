### Running the playbook
By default the existing containers whose name starts with ubuntu* or centos* will not be deleted
```
ansible-playbook provision-docker-containers.yml
```

If you wish to delete the existing containers with names either starting with ubuntu* or centos* and start provisioning
```
ansible-playbook provision-docker-containers.yml -e delete_containers=yes
```

### Passing multiple extra variables to playbook from CLI
```
ansible-playbook provision-docker-containers.yml -e delete_containers=yes -e second_var=1
ansible-playbook provision-docker-containers.yml -e "delete_container=yes second_var=1"
```

### Building docker images via ansible playbook
By default it won't delete the existing containers and images.
```
ansible-playbook build-docker-images
ansible-playbook build-docker-images -e delete_images=yes
ansible-playbook build-docker-images -e delete_images=no
```
