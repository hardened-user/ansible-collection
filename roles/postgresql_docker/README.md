# PostgreSQL - relational database management system (RDBMS)

Simple installation compatible with the [official Docker image](https://hub.docker.com/_/postgres)


## Variables
#### postgresql_version
Версия **postgresql**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
postgresql_version: "17"

# example
postgresql_version: "17.2"
```

#### postgresql_docker_build_template
Шаблон **Dockerfile** для сборки образа. Опционально.<br/>
См. [docker compose build specification](https://docs.docker.com/reference/compose-file/build/).
```
# default
postgresql_docker_build_template: ""

# example
postgresql_docker_build_template: "{{ role_path }}/templates/build/pg_probackup.j2"
```

#### postgresql_docker_instance
Имя экземпляра **postgresql**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
postgresql_docker_instance: "{{ postgresql_major_version }}"
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

#### postgresql_docker_conf_dir
Каталог для хранения конфигурации на диске.
```
# default
postgresql_docker_conf_dir: "{{ postgresql_docker_compose_dir }}/conf"
```

#### postgresql_docker_data_dir
Каталог для хранения данных на диске.<br/>
Используется если `postgresql_docker_bind_mount_volumes: true`
```
# default
postgresql_docker_data_dir: "{{ postgresql_docker_compose_dir }}/data"
```

#### postgresql_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
postgresql_docker_extra_volumes: []

# example
postgresql_docker_extra_volumes:
  - "/mnt/data0:/pg_probackup"
```

#### postgresql_extra_users
Список пользователей, который дополнительно будут созданы.<br/>
Элементом списка является словарь со следующими ключами:
* `name` - имя пользователя (обязательно)
* `pass` - пароль пользователя (обязательно)
* `base` - имя базы данных, которая будет создана (опционально)
* `attr` - аттрибуты пользователя. См. [role_attr_flags](https://docs.ansible.com/ansible/latest/collections/community/postgresql/postgresql_user_module.html#parameter-role_attr_flags) (опционально, default: `LOGIN`)
```
# default
postgresql_extra_users: []
```

#### postgresql_config
Пользовательская конфигурация `postgresql.conf`.<br/>
Перезаписывает `postgresql_conf_default`, значение `null` удалит переменную.
```
# default
postgresql_config: {}
```

#### postgresql_conf_default
Конфигурация `postgresql.conf` по-умолчанию.
```
# default
postgresql_conf_default:
  ...
```

#### postgresql_pg_hba_conf_list
Пользовательская конфигурация `pg_hba.conf`.
```
# default
postgresql_pg_hba_conf_list:
  - "local   replication     all                       trust"
  - "local   all             all                       trust"
  - "host    replication     all       127.0.0.1/32    trust"
  - "host    replication     all       ::1/128         trust"
  - "host    all             all       all             {{ postgresql_conf_default.password_encryption }}"
```

#### postgresql_tls_enabled
Использовать TLS при подключении к `postgresql`.
```
# default
postgresql_tls_enabled: false
```

#### postgresql_tls_cert_crt
Сертификат.
```
# default
postgresql_tls_cert_crt: |-
```

#### postgresql_tls_cert_key
Приватный ключ от сертификата.
```
# default
postgresql_tls_cert_key: |-
```


## Example
### Playbook
```
- name: "Setup PostgreSQL in Docker"
  hosts: locahost
  become: yes
  vars:
    postgresql_config:
      shared_buffers: 2GB
    postgresql_tls_enabled: true
    postgresql_tls_cert_crt: "{{ lookup('ansible.builtin.file', 'files/postgresql/{{ inventory_hostname }}/server.pem') }}"
    postgresql_tls_cert_key: "{{ lookup('ansible.builtin.file', 'files/postgresql/{{ inventory_hostname }}/server.key') }}"
    postgresql_extra_users:
      - name: "zabbix"
        pass: "zabbix"
        base: "zabbix"
  roles:
    - postgresql_docker
```
