# Keycloak

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/keycloak/keycloak)


## Variables
#### keycloak_version
Версия **keycloak**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
keycloak_version: "26.1"
```

#### keycloak_docker_instance
Имя экземпляра **keycloak**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
keycloak_docker_instance: "{{ keycloak_major_version }}"
```

#### keycloak_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
keycloak_docker_uid: 1000
```

#### keycloak_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
keycloak_docker_gid: 1000
```

#### keycloak_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
keycloak_docker_network: bridge
```

#### keycloak_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
keycloak_docker_bind_mount_volumes: true
```

#### keycloak_docker_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `keycloak_docker_bind_mount_volumes == true`.
```
# default
keycloak_docker_data_dir: "{{ keycloak_docker_compose_dir }}/data"
```

#### keycloak_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
keycloak_docker_extra_volumes: []

# example
keycloak_docker_extra_volumes:
  - "/host/path:/container/path"
```

#### keycloak_docker_listen_addr
IP адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` означает, что будут использоваться все адреса.<br/>
Используется если `keycloak_docker_network == bridge`.
```
# default
keycloak_docker_listen_addr: "0.0.0.0"
```

#### keycloak_docker_listen_port
Номера портов, которые будут перенаправлены в контейнер.<br/>
Используется если `keycloak_docker_network == bridge`.
```
# default
keycloak_docker_listen_port: ["{{ keycloak_http_port }}", "{{ keycloak_http_management_port }}" ]
```

#### keycloak_docker_environment
Пользовательская конфигурация переменных окружения.<br/>
Перезаписывает `keycloak_docker_env_default`, значение `null` удалит переменную.
```
# default
keycloak_docker_environment: {}
```

#### keycloak_docker_env_default
Переменные окружения по-умолчанию.
```
# default
keycloak_docker_env_default:
  KC_PROXY_HEADERS: xforwarded
```


## Note
You are logged in as a temporary admin user. To harden security, create a permanent admin account and delete the temporary one.

```
$ docker compose exec keycloak bash
$ cd /opt/keycloak/bin
$ ./kcadm.sh config credentials --server http://localhost:8017 --realm master --user "${KC_BOOTSTRAP_ADMIN_USERNAME}" --password "${KC_BOOTSTRAP_ADMIN_PASSWORD}"
Logging into http://localhost:8017 as user temp-admin of realm master
$ ./kcadm.sh create users -r master -s username=new-admin -s enabled=true
$ ./kcadm.sh set-password -r master --username new-admin --new-password "*****"
$ ./kcadm.sh add-roles -r master --uusername new-admin --rolename admin
```

```
$ ./kcadm.sh get users -r master
$ ./kcadm.sh delete -r master users/<user_id>
```


## Example
### Playbook
```
- name: "Setup Keycloak in Docker"
  hosts: locahost
  become: yes
  roles:
    - keycloak_docker
```
