# Telegram Messenger MTProto zero-configuration proxy server.

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/telegrammessenger/proxy/)


## Variables
#### mtproxy_docker_version
Версия **mtproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
mtproxy_docker_version: "latest"
```

#### mtproxy_docker_build_template
Шаблон **Dockerfile** для сборки образа. Опционально.<br/>
См. [docker compose build specification](https://docs.docker.com/reference/compose-file/build/).
```
# default
mtproxy_docker_build_template: ""

# example
mtproxy_docker_build_template: "{{ role_path }}/templates/build/Dockerfile.j2"
```

#### mtproxy_docker_instance
Имя экземпляра **mtproxy**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
mtproxy_docker_instance: ""
```

#### mtproxy_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
mtproxy_docker_compose_extra_conf: {}

# example
mtproxy_docker_compose_extra_conf:
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

#### mtproxy_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
mtproxy_docker_extra_volumes: []
```

#### mtproxy_docker_conf_dir
Каталог для хранения данных на диске.<br/>
```
# default
mtproxy_docker_conf_dir: "{{ mtproxy_docker_compose_dir }}/conf"
```

#### mtproxy_docker_environment
Пользовательская конфигурация переменных окружения.<br/>
Перезаписывает `mtproxy_docker_env_default`, значение `null` удалит переменную.
```
# default
mtproxy_docker_environment: {}
```

#### mtproxy_docker_env_default
Переменные окружения по-умолчанию.
```
# default
mtproxy_docker_env_default: {}
```


## Example
### Playbook
```
- name: "Setup MTProxy in Docker"
  hosts: locahost
  become: yes
  roles:
    - mtproxy_docker
```
