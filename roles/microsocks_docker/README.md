# MicroSocks - multithreaded, small, efficient SOCKS5 server

Simple installation compatible with the [hardeneduser/microsocks](https://hub.docker.com/r/hardeneduser/microsocks)


## Variables
#### microsocks_docker_version
Версия **microsocks**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
microsocks_docker_version: "1.0.5"
```

#### microsocks_docker_tag
Явное указание docker tag.<br/>
```
# default
microsocks_docker_tag: "{{ microsocks_docker_version }}"
```

#### microsocks_docker_instance
Имя экземпляра **microsocks**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
microsocks_docker_instance: ""
```

#### microsocks_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
microsocks_docker_compose_extra_conf: {}

# example
microsocks_docker_compose_extra_conf:
  deploy:
    resources:
      limits:
        cpus: "1"
        memory: "512M"
      reservations:
        memory: "64M"
  logging:
    driver: "json-file"
    options:
      max-size: "8m"
```

#### microsocks_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
microsocks_docker_extra_volumes: []
```

#### microsocks_docker_listen_addr
IP адрес для приёма входящих подключений.<br/>
Значение `0.0.0.0` означает все доступные адреса.
```
# default
microsocks_docker_listen_addr: "0.0.0.0"
```

#### microsocks_docker_listen_port
Номер порта, который будет использован контейнером для входящих подключений.
```
# default
microsocks_docker_listen_port: 1080
```

#### microsocks_docker_command
Конфигурация `config.toml`.<br/>
```
# default
microsocks_docker_command: ["-i", "{{ microsocks_docker_listen_addr }}", "-p", "{{ microsocks_docker_listen_port }}"]
```


## Example
### Playbook
```
- name: "Setup MicroSocks in Docker"
  hosts: locahost
  become: yes
  vars:
    microsocks_docker_command: ["-p", "{{ microsocks_docker_listen_port }}", "-u", "user", "-P", "*****", "-b", "10.10.0.5"]
    microsocks_docker_compose_extra_conf:
    dns:
      - 10.10.0.1
  roles:
    - microsocks_docker
```
