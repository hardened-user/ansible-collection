# Zabbix Web Interface with PostgreSQL database support

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/zabbix/zabbix-web-nginx-pgsql)


## Variables
#### zabbix_web_nginx_pgsql_version
Версия **Zabbix Web Interface**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
zabbix_web_nginx_pgsql_version: "7.0"
```


#### zabbix_server_pgsql_docker_environment
Переменные окружения docker контейнера.
```
# default
zabbix_server_pgsql_docker_environment: {}

# example
zabbix_server_pgsql_docker_environment:
  ZBX_MEMORYLIMIT: 128M
```


## Example
### Playbook
```
- name: "Setup Zabbix Web Interface in Docker"
  hosts: locahost
  become: yes
  vars:
    zabbix_server_pgsql_docker_environment:
      ENABLE_WEB_ACCESS_LOG: "false"
  roles:
    - zabbix_web_nginx_pgsql_docker
```
