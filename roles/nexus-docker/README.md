# Sonatype Nexus

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/sonatype/nexus3)


## Variables
#### nexus_version
Версия **nexus**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
nexus_version: "3.65.0"
```

#### nexus_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
nexus_docker_uid: 200
```

#### nexus_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
nexus_docker_gid: 200
```

#### nexus_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
nexus_docker_bind_mount_volumes: true
```

#### nexus_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
nexus_docker_extra_volumes: []
```

#### nexus_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `nexus_docker_bind_mount_volumes: true`
```
# default
nexus_data_dir: "{{ nexus_docker_compose_dir }}/data"
```


## Example
### Playbook
```
- name: "Setup Sonatype Nexus in Docker"
  hosts: locahost
  become: yes
  roles:
    - nexus-docker
```
