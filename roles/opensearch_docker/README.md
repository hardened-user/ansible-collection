# OpenSearch

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/opensearchproject/opensearch)


## Variables
#### opensearch_version
Версия **opensearch**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
opensearch_version: "2.19.3"
```

#### opensearch_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
opensearch_docker_uid: 1000
```

#### opensearch_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
opensearch_docker_gid: 1000
```

#### opensearch_docker_instance
Имя экземпляра **opensearch**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
opensearch_docker_instance: ""

# example
opensearch_docker_instance: "{{ opensearch_version.split('.')[:2] | join('.') }}"
```

#### opensearch_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
opensearch_docker_network: bridge
```

#### opensearch_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
opensearch_docker_compose_extra_conf: {}

# example
opensearch_docker_compose_extra_conf:
  deploy:
    resources:
      limits:
        cpus: "4"
        memory: "8192M"
      reservations:
        cpus: "0.25"
        memory: "4096M"
  logging:
    driver: "json-file"
    options:
      max-size: "8m"
```

#### opensearch_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
opensearch_docker_bind_mount_volumes: true
```

#### opensearch_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
opensearch_docker_extra_volumes: []
```

#### opensearch_docker_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `opensearch_docker_bind_mount_volumes: false`
```
# default
opensearch_docker_data_dir: "{{ opensearch_docker_compose_dir }}/data"
```

#### opensearch_docker_logs_dir
Каталог для хранения логов на диске.<br/>
Используется если `opensearch_docker_bind_mount_volumes: false`
```
# default
opensearch_docker_logs_dir: "{{ opensearch_docker_compose_dir }}/logs"
```

#### opensearch_plugins_security_enabled
Использовать **security-plugin**.
```
# default
opensearch_plugins_security_enabled: true
```

#### opensearch_plugins_security_ssl_http_enabled
Позволяет отключить требование использовать шифрование трафика (**https**).<br/>
Используется если `opensearch_plugins_security_enabled: true`
```
# default
opensearch_plugins_security_ssl_http_enabled: false
```

#### opensearch_initial_admin_password
Пароль для встроенного пользователя **admin** при первоначально настройке.<br/>
Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.<br/>
Используется если `opensearch_plugins_security_enabled: true`
```
# default
opensearch_initial_admin_password: ""
```

#### opensearch_docker_environment
Пользовательская конфигурация переменных окружения.<br/>
Перезаписывает `opensearch_docker_env_default`, значение `null` удалит переменную.
```
# default
opensearch_docker_environment: {}
```


## Example
### Playbook
```
- name: "Setup OpenSearch in Docker"
  hosts: locahost
  become: yes
  vars:
    opensearch_initial_admin_password: !vault |
      $ANSIBLE_VAULT;1.1;AES256
      38636564636362396136383762303936616531383438643462383136646431613733376263353763
      38636564636362396136383762303936616531383438643462383136646431613733376263353763
      38636564636362396136383762303936616531383438643462383136646431613733376263353763
      38636564636362396136383762303936616531383438643462383136646431613733376263353763
      34373136396538653031623039363139373065613265316639383363636265333131
    opensearch_docker_environment:
      OPENSEARCH_JAVA_OPTS: "-Xms2048m -Xmx4096m"
  roles:
    - opensearch-docker
```
