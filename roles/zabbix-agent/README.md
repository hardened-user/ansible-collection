# Zabbix Agent


## Variables
#### zabbix_agent_user_extra_groups
Имя или список групп, в которые будет добавлен пользователь `{{ zabbix_agent_user_name }}`.
```
# default
zabbix_agent_user_extra_groups: []
```


## Example
### Playbook
```
- name: "Setup Zabbix Agent"
  hosts: locahost
  become: yes
  roles:
    - zabbix-agent
```
