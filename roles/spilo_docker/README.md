# Spilo by Zalando

Simple installation compatible with the [official Docker image](https://github.com/zalando/spilo)


## Variables
#### spilo_version
Версия **spilo**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
spilo_version: "17"
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
spilo_docker_instance: "{{ spilo_version }}"
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
Используется если `spilo_docker_bind_mount_volumes: false`
```
# default
spilo_docker_data_dir: "{{ spilo_docker_compose_dir }}/data"
```

#### spilo_docker_environment
Переменные окружения docker контейнера.
```
# default
spilo_docker_environment: {}

# example
spilo_docker_environment:
  SCOPE: "mycluster"
  APIPORT: 8008
```


## Example
### Playbook
```
- name: "Setup Spilo by Zalando in Docker"
  hosts: locahost
  become: yes
  vars:
    ETCD3_HOSTS: "etcd-01:2379,etcd-02:2379,etcd-03:2379"
  roles:
    - spilo_docker
```
