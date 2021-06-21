### Running the playbook
This expects the inventory file with ansible_become_user=tektutor ansible_become_password=tektutor and playbook with become: yes

```
ansible-playbook sudo-elevation-playbook.yml
```

### Running the playbook without become_password in the inventory
In this case, you just need to mention the ansible_become_user and ansible_become_password can be removed from the inventory(hosts) file.
```
ansible-playbook sudo-elevation-playbook.yml --ask-become-pass
```
### Running the playbook
In this case, you don't need to mention become: yes in the playbook.  You don't need to mention ansible_become_user and ansible_become_password as the details are supplied in the command line.
```
ansible-playbook sudo-elevation-playbook.yml -b --become-user root --ask-become-pass
```
