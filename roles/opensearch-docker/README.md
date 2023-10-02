# OpenSearch

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/opensearchproject/opensearch)


## Variables
#### opensearch_version
Версия **opensearch**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
opensearch_version: "2.8.0"
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

#### opensearch_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
opensearch_docker_network: bridge
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

#### opensearch_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `opensearch_docker_bind_mount_volumes: false`
```
# default
opensearch_data_dir: "{{ opensearch_docker_compose_dir }}/data"
```

#### opensearch_logs_dir
Каталог для хранения логов на диске.<br/>
Используется если `opensearch_docker_bind_mount_volumes: false`
```
# default
opensearch_logs_dir: "{{ opensearch_docker_compose_dir }}/logs"
```

#### opensearch_conf_dict
Произвольная конфигурация `opensearch.yml`.<br/>
Параметры, через переменные окружения, подставляются скриптом `opensearch-docker-entrypoint.sh` в аргументы командной строки.
```
# default
opensearch_conf_dict: {}
```


## Example
### Playbook
```
- name: "Setup OpenSearch in Docker"
  hosts: locahost
  become: yes
  roles:
    - opensearch-docker
```
