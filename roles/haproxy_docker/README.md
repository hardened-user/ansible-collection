# HAProxy

Simple installation HAProxy with the [official Docker image](https://hub.docker.com/_/haproxy/)

## Variables
#### haproxy_version
Версия **haproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
haproxy_version: "1.125.1"
```

#### haproxy_docker_instance
Имя экземпляра **haproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
haproxy_docker_instance: ""
```


## Example
### Playbook
```
- name: "Setup HAProxy in Docker"
  hosts: locahost
  become: yes
  vars:
    haproxy_docker_network: host
    haproxy_config_template: "files/haproxy/{{ inventory_hostname }}/haproxy.cfg.j2"
  roles:
    - haproxy_docker
```
