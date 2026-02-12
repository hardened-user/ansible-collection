# Spilo by Zalando

Simple installation compatible with the [official Docker image](https://github.com/zalando/spilo)


## Variables
#### spilo_docker_version
Версия **spilo**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
spilo_docker_version: "17"
```

#### spilo_docker_tag
Тег образа, указывает на конкретную сборку.<br/>
```
# default
spilo_docker_tag: "latest"
```

#### spilo_docker_instance
Имя экземпляра **spilo**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
spilo_docker_instance: "{{ spilo_docker_version }}"
```

#### spilo_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
spilo_docker_uid: 101
```

#### spilo_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
spilo_docker_gid: 103
```

#### spilo_docker_compose_extra_conf
Дополнительные параметры для сервиса в **docker-compose**.
```
# default
spilo_docker_compose_extra_conf: {}

# example
spilo_docker_compose_extra_conf:
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

#### spilo_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
spilo_docker_bind_mount_volumes: true
```

#### spilo_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
spilo_docker_extra_volumes: []
```

#### spilo_docker_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `spilo_docker_bind_mount_volumes: true`
```
# default
spilo_docker_data_dir: "{{ spilo_docker_compose_dir }}/data"
```

### spilo_docker_postgresql_listen_port
Номер порта для подключения к Postgres.
```yaml
# default
spilo_docker_postgresql_listen_port: 5432

```

### spilo_docker_patroni_restapi_listen_port
Номер порта для подключения к Patroni REST API.
```yaml
# default
spilo_docker_patroni_restapi_listen_port: 8008
```

#### spilo_docker_extra_users
Список пользователей, который дополнительно будут созданы.<br/>
Элементом списка является словарь со следующими ключами:
* `name` - имя пользователя (обязательно)
* `pass` - пароль пользователя (обязательно)
* `base` - имя базы данных, которая будет создана (опционально)
* `attr` - аттрибуты пользователя. См. [role_attr_flags](https://docs.ansible.com/ansible/latest/collections/community/postgresql/spilo_docker_postgresql_user_module.html#parameter-role_attr_flags) (опционально, default: `LOGIN`)
```
# default
spilo_docker_extra_users: []
```

### spilo_docker_sql_queries
Список SQL запросов, которые нужно выполнить.<br/>
Элементом списка является словарь со следующими ключами:
* `exec` - текст выполняемого запроса (обязательно)
* `base` - база данных для выполнения (опционально, default: `postgres`)
```yaml
# default
spilo_docker_sql_queries: []
```

#### spilo_docker_dcs_conf
Настройки динамической конфигурации, после инициализации кластера можно поменять только через `patronictl`.<br/>
Изменения происходят командой `patronictl edit-config --apply`!!!<br/>
См. [Dynamic Configuration Settings](https://patroni.readthedocs.io/en/latest/dynamic_configuration.html).
```
# default
spilo_docker_dcs_conf: {}

# example
spilo_docker_dcs_conf:
  ttl: 15
  synchronous_mode: true
```

#### spilo_docker_environment
Переменные окружения docker контейнера.
```
# default
spilo_docker_environment: {}

# example
spilo_docker_environment:
  ETCD3_HOSTS: "etcd-01:2379,etcd-02:2379,etcd-03:2379"
```


## Example
### Playbook
```
- name: "Setup Spilo by Zalando in Docker"
  hosts: locahost
  become: yes
  vars:
    spilo_docker_superuser_pass: "PaS$w0rd"
    spilo_docker_environment:
      ETCD3_HOSTS: "etcd-01:2379,etcd-02:2379,etcd-03:2379"
      SPILO_CONFIGURATION:
        bootstrap:
          dcs:
            synchronous_mode: true
            postgresql:
              parameters:
                max_connections: 999
  roles:
    - spilo_docker
```
