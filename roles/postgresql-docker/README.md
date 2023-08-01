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

#### postgresql_docker_bind_mount_volumes
Если значение `true` - данные будут храниться в каталоге `postgresql_data_dir`.<br/>
Если значение `false` - данные будут храниться в **docker volume**.
```
# default
postgresql_docker_bind_mount_volumes: true
```

#### postgresql_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `postgresql_docker_bind_mount_volumes: false`
```
# default
postgresql_data_dir: "{{ postgresql_setup_dir }}/data"
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

#### postgresql_conf_src
Конфигурация **PostgreSQL** осуществляется путем копирования файлов из каталога `postgresql_conf_src`.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
postgresql_conf_src: "{{ role_path }}/files/{{ postgresql_major_version }}"

# example
postgresql_conf_src: "files/postgresql-docker/{{ inventory_hostname }}/{{ postgresql_major_version }}"
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
