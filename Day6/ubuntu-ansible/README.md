### Running the playbook
```
ansible-playbook sudo-elevation-playbook.yml
```

### Running the playbook without become_password in the inventory
In this case, you just need to mention the ansible_become_user and ansible_become_password can be removed from the inventory(hosts) file.
```
ansible-playbook sudo-elevation-playbook.yml --ask-become-pass
```
