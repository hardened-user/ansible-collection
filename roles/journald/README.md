# Journald


## Variables
#### journald_system_max_use
Максимальный размер всех хранимых файлов журналов.<br/>
При превышении, наиболее старые будут удаляться.
```
journald_system_max_use: "512M"
journald_system_max_use: "1G"
```


## Example
### Playbook
```
- name: "Setup Journald"
  hosts: locahost
  become: yes
  roles:
    - journald
```
