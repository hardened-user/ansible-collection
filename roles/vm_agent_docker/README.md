# VictoriaMetrics Agent (VMAgent)

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/victoriametrics/vmagent)


## Variables
#### vm_agent_docker_version
Версия **VMAgent**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_agent_docker_version: "1.140.0"
```

#### vm_agent_docker_instance
Имя экземпляра **VMAgent**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vm_agent_docker_instance: ""
```


## Example
### Playbook
```
- name: "Setup VMAgent in Docker"
  hosts: locahost
  become: yes
  vars:
    vm_agent_docker_conf_d_src: "files/vm_agent_docker/{{ inventory_hostname }}/conf.d"
    vm_agent_docker_config:
      remoteWrite.url: "http://victoriametrics:8428/api/v1/write"
  roles:
    - vm_agent_docker
```
