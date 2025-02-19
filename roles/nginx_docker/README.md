# Nginx

Simple installation compatible with the [official Docker image](https://hub.docker.com/_/nginx)


## Variables
#### nginx_version
Версия **nginx**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
nginx_version: "1.26"
```

#### nginx_docker_instance
Имя экземпляра **nginx**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
nginx_docker_instance: ""
```

#### nginx_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
nginx_docker_uid: 33
```

#### nginx_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
nginx_docker_gid: 33
```

#### nginx_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
nginx_docker_network: bridge
```

#### nginx_docker_cert_dir
Каталог для хранения сертификатов на диске.
```
# default
nginx_docker_cert_dir: "{{ nginx_docker_compose_dir }}/cert"
```

#### nginx_docker_conf_dir
Каталог для хранения конфигурации на диске.
```
# default
nginx_docker_conf_dir: "{{ nginx_docker_compose_dir }}/conf"
```

#### nginx_docker_data_dir
Каталог для хранения данных на диске.
```
# default
nginx_docker_data_dir: "{{ nginx_docker_compose_dir }}/data"

# example
nginx_docker_data_dir: "/var/www"
```

#### nginx_docker_logs_dir
Каталог для хранения логов на диске.
```
# default
nginx_docker_logs_dir: "{{ nginx_docker_compose_dir }}/logs"
```

#### nginx_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
nginx_docker_extra_volumes: []
```

#### nginx_docker_tmpfs_volumes
Список `tmpfs` разделов в контейнере.
```
# default
nginx_docker_tmpfs_volumes: []

# example
nginx_docker_tmpfs_volumes:
  - "/var/cache/nginx:noatime,nodiratime,nodev,nosuid,noexec,uid=0,gid=0,mode=755,size=32m"
```

#### nginx_docker_cert_src
Каталог, откуда будут скопированы сертификаты.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
nginx_docker_cert_src: "{{ role_path }}/files/cert"
```

#### nginx_docker_conf_src
Каталог, откуда будут скопированы файлы конфигурации.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
nginx_docker_conf_src: "{{ role_path }}/files/conf"

# example
nginx_docker_conf_src: "files/nginx/{{ inventory_hostname }}/conf"
```

#### nginx_docker_data_src
Каталог, откуда будут скопированы файлы данных.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
nginx_docker_data_src: "{{ role_path }}/files/data"

# example
nginx_docker_data_src: "files/nginx/{{ inventory_hostname }}/data"
```

#### nginx_docker_logrotate_interval
Частота ротации логов.<br/>
См. `man logrotate`
```
# default
nginx_docker_logrotate_interval: "daily"
```

#### nginx_docker_logrotate_rotate
Количество архивных файлов, которые будут сохранены.
```
# default
nginx_docker_logrotate_rotate: 31
```

#### nginx_docker_listen_addr
IP адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` означает, что будут использоваться все адреса.<br/>
Используется если `nginx_docker_network == bridge`.
```
# default
nginx_docker_listen_addr: "0.0.0.0"

# example
nginx_docker_listen_addr: "127.0.0.1"
```

#### nginx_docker_listen_port
Номера портов, которые будут перенаправлены в контейнер.<br/>
Используется если `nginx_docker_network == bridge`.
```
# default
nginx_docker_listen_port: [80, 443]
```


## Example
### Playbook
```
- name: "Setup Nginx in Docker"
  hosts: locahost
  become: yes
  vars:
    nginx_docker_data_dir: "/var/www"
    nginx_docker_extra_volumes:
      - "{{ php_fpm_docker_fpm_sock_dir }}:{{ php_fpm_docker_fpm_sock_dir }}"
      - "{{ getssl_cert_dir }}:{{ getssl_cert_dir }}:ro"
      - "{{ getssl_acme_challenge_dir }}:/.well-known/acme-challenge:ro"
    nginx_docker_conf_src: "files/nginx/{{ inventory_hostname }}/conf"
    nginx_docker_data_src: "files/nginx/{{ inventory_hostname }}/data"
  roles:
    - nginx_docker
```
