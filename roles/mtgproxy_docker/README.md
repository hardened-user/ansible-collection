# Highly-opinionated MTPROTO proxy for Telegram

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/nineseconds/mtg)


## Variables
#### mtgproxy_docker_version
Версия **mtgproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
mtgproxy_docker_version: "2"
```

#### mtgproxy_docker_instance
Имя экземпляра **mtgproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
mtgproxy_docker_instance: ""
```

#### mtgproxy_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
mtgproxy_docker_compose_extra_conf: {}

# example
mtgproxy_docker_compose_extra_conf:
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

#### mtgproxy_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
mtgproxy_docker_extra_volumes: []
```

#### mtgproxy_docker_config
Конфигурация `config.toml`.<br/>
```
# default
mtgproxy_docker_config: "{{ lookup('template', 'config.toml.j2') }}"
```


## Example
### Secret
```
$ docker run --rm nineseconds/mtg:2 generate-secret -x google.com
eedabbf38191eeaad42d178f90968d0898676f6f676c652e636f6d
```


### Playbook
```
- name: "Setup MTG in Docker"
  hosts: locahost
  become: yes
  vars:
    mtgproxy_docker_config: "{{ lookup('template', 'files/mtgproxy/' + inventory_hostname + '/config.toml') }}"
  roles:
    - mtgproxy_docker
```
