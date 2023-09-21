# PostgreSQL - relational database management system (RDBMS)

Simple installation compatible with the [official Docker image](https://hub.docker.com/_/postgres)


## Variables
#### postgresql_version
Версия **PostgreSQL**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
postgresql_version: "14"

# example
postgresql_version: "14.8"
```

#### postgresql_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
postgresql_docker_uid: 999
```

#### postgresql_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
postgresql_docker_gid: 999
```

#### postgresql_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
postgresql_docker_network: bridge
```

#### postgresql_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
postgresql_docker_bind_mount_volumes: true
```

#### postgresql_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
postgresql_docker_extra_volumes: []

# example
postgresql_docker_extra_volumes:
  - "/mnt/data0:/mnt/tablespace"
```

#### postgresql_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `postgresql_docker_bind_mount_volumes: false`
```
# default
postgresql_data_dir: "{{ postgresql_docker_compose_dir }}/data"
```

#### postgresql_conf_dict
Конфигурация `postgresql.conf`.<br/>
```
# default
postgresql_conf_dict: {}
```

#### postgresql_pg_hba_conf_list
Конфигурация `pg_hba.conf`.<br/>
```
# default
postgresql_pg_hba_conf_list:
  - "local   replication     all                       trust"
  - "local   all             all                       trust"
  - "host    replication     all       127.0.0.1/32    trust"
  - "host    replication     all       ::1/128         trust"
  - "host    all             all       all             {{ postgresql_conf_default.password_encryption }}"
```


## Example
### Playbook
```
- name: "Setup PostgreSQL in Docker"
  hosts: locahost
  become: yes
  roles:
    - postgresql-docker
```
