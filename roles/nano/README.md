# Nano

The role sets the parameters and enable all the existing definitions of syntax.
```
set historylog
set locking
set noconvert
```

## Example
### Playbook
```
- name: "Setup Nano Text Editor"
  hosts: localhost
  become: yes
  roles:
    - nano
```
