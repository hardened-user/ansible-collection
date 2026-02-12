# Vector

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/timberio/vector)


## Variables
#### vector_docker_version
Версия **vector**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vector_docker_version: "0.51.1-alpine"
```

#### vector_docker_instance
Имя экземпляра **vector**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
vector_docker_instance: ""
```

#### vector_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
vector_docker_compose_extra_conf: {}

# example
vector_docker_compose_extra_conf:
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

#### vector_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
vector_docker_bind_mount_volumes: true
```

#### vector_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
vector_docker_extra_volumes: []
```

#### vector_docker_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `vector_docker_bind_mount_volumes: true`
```
# default
vector_docker_data_dir: "{{ vector_docker_compose_dir }}/data"
```

#### vector_docker_config
Конфигурация `vector.yaml`.<br/>
```
# default
vector_docker_config:

# example
vector_docker_config:
  sources:
    logs:
      ...
  sinks:
    elasticsearch:
      ...
```


## Example
### Playbook
```
- name: "Setup Vector in Docker"
  hosts: locahost
  become: yes
  vars:
    vector_docker_extra_volumes:
      - "/var/log:/var/log:ro"
    vector_docker_config: "{{ lookup('template', 'files/vector/' + inventory_hostname + '/vector.yaml') }}"
  roles:
    - vector_docker
```
