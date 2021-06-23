### Create an ansible.cfg under Day8/AnsibleVault folder with the below content
```
[defaults]
deprecation_warnings=False
inventory=./dynamic_inventory.py
vault_password_file=.vault_password
```

### Create a .vault_password file in Day8/AnsibleVault folder with any password
```
root@123
```
Technically speaking the .vault_password filename is user-defined, hence feel free to name the file as per your preference. 
Just make sure, the same file name is updated in the ansible.cfg file. The password is user-defined :)

### Creating your vault protected file
```
ansible-vault create credentials.yml
```

### Encrypting your vault protected file
```
ansible-vault encrypt credentials.yml
```

### Decrypting your vault protected file
```
ansible-vault decrypt credentials.yml
```

### Editing your vault protected file
```
ansible-vault edit credentials.yml
```

### Viewing your vault protected file
```
ansible-vault view credentials.yml
```

### Accessing the vault protected credentials from ansible playbook
```
ansible-playbook playbook.yml
```

### The below playbook demonstrates securing ansible_become_user and ansible_become_password with ansible-vault
The credentials.yml file look as shown below
```
login_credentials:
   user: ansible
   password: tower@123
   ansible_become_user: root
   ansible_become_password: tektutor 
```

### In case you don't prefer storing the vault password in a file
```
ansible-playbook playbook.yml --ask-vault-pass
```

### The below playbook demonstrates securing ansible_become_user and ansible_become_password with ansible-vault
```
ansible-playbook install-vim.yml 
```
The credentials.yml file look as shown below
```
login_credentials:
   user: ansible
   password: tower@123
   ansible_become_user: root
   ansible_become_password: tektutor 

ansible_become_user: root
ansible_become_password: tektutor 
```

### See if you can use an encrypted inventory file
```
ansible-vault encrypt hosts
ansible-playbook install-vim.yml
```

### See if you can use an encrypted inventory and encrypted playbook
```
ansible-vault encrypt install-vim.yml
ansible-playbook install-vim.yml
```
