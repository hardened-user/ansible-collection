# node_exporter

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/prom/node-exporter)


## Variables
#### node_exporter_version
Версия **node_exporter**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
node_exporter_version: "1.9.1"
```

#### node_exporter_docker_listen_addr
IP адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` означает, что будут использоваться все адреса.
```
# default
node_exporter_docker_listen_addr: "0.0.0.0"
```

#### node_exporter_docker_listen_port
Номера портов, которые будут перенаправлены в контейнер.
```
# default
node_exporter_docker_listen_port: 9100
```

#### node_exporter_flags
Список флагов, позволяет настраивать `node_exporter`.<br/>

```
# default
node_exporter_flags:
  - "--collector.filesystem.mount-points-exclude=^/(dev|proc|run|sys|var/lib/docker/.+|var/lib/kubelet/.+)($|/)"
```


## Example
### Playbook
```
- name: "Setup node_exporter in Docker"
  hosts: locahost
  become: yes
  roles:
    - node_exporter_docker
```
