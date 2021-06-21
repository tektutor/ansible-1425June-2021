### Running the playbook - Handlers and Notifiers
```
cd Day6/HandlersAndNotifiers/
ansible-playbook install-nginx-playbook.yml
```
The handler will be invoked only when the installation is done fresh. Subsequents attempts to install will not invoke the handler task.
