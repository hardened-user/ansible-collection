# Zabbix Official Repository

https://repo.zabbix.com/ setup from `zabbix-release` vendor package.


## Variables
#### zabbix_repo_version
Версия **Zabbix**.<br/>
Используется как базовое значение для определения URL репозитория.
```
zabbix_repo_version: "6.4"
```


## Example
### Playbook
```
- name: "Setup Zabbix Official Repository"
  hosts: locahost
  become: yes
  roles:
    - zabbix-repo
```
