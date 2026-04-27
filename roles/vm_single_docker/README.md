# VictoriaMetrics Single (VMSingle)

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/victoriametrics/victoria-metrics)


## Variables
#### vm_single_docker_version
Версия **VMSingle**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_single_docker_version: "1.140.0"
```

#### vm_single_docker_instance
Имя экземпляра **VMSingle**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_single_docker_instance: ""
```


## Example
### Playbook
```
- name: "Setup VMSingle in Docker"
  hosts: locahost
  become: yes
  roles:
    - vm_single_docker
```
