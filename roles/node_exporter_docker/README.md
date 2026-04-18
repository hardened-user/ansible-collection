# node_exporter

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/prom/node-exporter)


## Variables
#### node_exporter_docker_version
Версия **node_exporter**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
node_exporter_docker_version: "1.11.1"
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

#### node_exporter_docker_conf
Список флагов, позволяет настраивать `node_exporter`.<br/>

```
# default
node_exporter_docker_conf_default:
  log.level: "info"
  collector.filesystem.mount-points-exclude: "^/(dev|proc|run|sys|var/lib/docker/.+|var/lib/kubelet/.+)($|/)"
```


## Example
### Playbook
```
- name: "Setup node_exporter in Docker"
  hosts: locahost
  become: yes
  vars:
    node_exporter_docker_compose_extra_conf:
      deploy:
        resources:
          limits:
            cpus: "0.5"
            memory: "256M"
          reservations:
            memory: "64M"
  roles:
    - node_exporter_docker
```
