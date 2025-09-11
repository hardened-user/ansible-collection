# VictoriaMetrics

Simple installation VictoriaMetrics Single with the [official Docker image](https://hub.docker.com/r/victoriametrics/victoria-metrics/)

## Variables
#### vm_single_version
Версия **VictoriaMetrics Single**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_single_version: "1.125.1"
```

#### vm_single_docker_instance
Имя экземпляра **VictoriaMetrics Single**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_single_docker_instance: ""
```


## Example
### Playbook
```
- name: "Setup VictoriaMetrics Single in Docker"
  hosts: locahost
  become: yes
  roles:
    - vm_single_docker
```
