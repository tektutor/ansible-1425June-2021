### Create a local git repo
```
git init
```

### Create a README.md file
```
touch README.md
echo "# This is a test file" > README.md
```

### Check the status
```
git status
```

### Stage changes
```
git add --all .
```

### Commit changes to local git repo
```
git commit -m "Initial commit."
git status
```

### Printing and setting git config details using ansible playbook
```
ansible-playbook git-config-playbook.yml
```
