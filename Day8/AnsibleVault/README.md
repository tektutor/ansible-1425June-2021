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

### In case you don't prefer storing the vault password in a file
```
ansible-playbook playbook.yml --ask-vault-pass
```
