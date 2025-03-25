# PHP-FPM

Simple installation compatible with the [official Docker image](https://hub.docker.com/_/php)


## Variables
#### php_fpm_version
Версия **php-fpm**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
php_fpm_version: "8.2"
```

#### php_fpm_docker_instance
Имя экземпляра **php-fpm**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
php_fpm_docker_instance: "{{ php_fpm_version.split('.')[0:2] | join('.') }}"
```

#### php_fpm_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
php_fpm_docker_uid: 33
```

#### php_fpm_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
php_fpm_docker_gid: 33
```

#### php_fpm_docker_php_conf_dir
Каталог для хранения конфигурации **php** на диске.
```
# default
php_fpm_docker_php_conf_dir: "{{ php_fpm_docker_compose_dir }}/php"
```

#### php_fpm_docker_fpm_conf_dir
Каталог для хранения конфигурации **php-fpm** на диске.
```
# default
php_fpm_docker_fpm_conf_dir: "{{ php_fpm_docker_compose_dir }}/php-fpm.d"
```

#### php_fpm_docker_fpm_sock_dir
Каталог для сокетов. Опционально.<br/>
В `php-fpm.d` указать `listen = /run/php-fpm/$pool.sock`.
```
# default
php_fpm_docker_fpm_sock_dir: ""

# example
php_fpm_docker_fpm_sock_dir: "/run/php-fpm-{{ php_fpm_version.split('.')[0:2] | join('.') }}"
```

#### php_fpm_docker_sessions_dir
Каталог для хранения сессий на диске. Опционально.<br/>
В `php.ini` указать путь внутри контейнера `session.save_path = "/var/lib/php/sessions"`.
```
# default
php_fpm_docker_sessions_dir: ""

# example
php_fpm_docker_sessions_dir: "{{ php_fpm_docker_compose_dir }}/sessions"
```

#### php_fpm_docker_logs_dir
Каталог для хранения логов на диске.
```
# default
php_fpm_docker_logs_dir: "{{ php_fpm_docker_compose_dir }}/logs"
```

#### php_fpm_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
php_fpm_docker_extra_volumes: []

# example
php_fpm_docker_extra_volumes:
  - "/var/www:/var/www"
```

#### php_fpm_docker_php_conf_src
Каталог, откуда будут скопированы файлы конфигурации **php**.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
php_fpm_docker_php_conf_src: "{{ role_path }}/files/{{ php_fpm_docker_instance }}/php"

# example
php_fpm_docker_php_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_docker_instance }}/php"
```

#### php_fpm_docker_fpm_conf_src
Каталог, откуда будут скопированы файлы конфигурации **php-fpm**.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
php_fpm_docker_fpm_conf_src: "{{ role_path }}/files/{{ php_fpm_docker_instance }}/php-fpm.d"

# example
php_fpm_docker_fpm_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_docker_instance }}/php-fpm.d"
```

#### php_fpm_docker_logrotate_interval
Частота ротации логов.<br/>
См. `man logrotate`
```
# default
php_fpm_docker_logrotate_interval: "daily"
```

#### php_fpm_docker_logrotate_rotate
Количество архивных файлов, которые будут сохранены.
```
# default
php_fpm_docker_logrotate_rotate: 31
```

#### php_fpm_docker_tcp_enabled
Разрешить проброс порта в контейнер.
```
# default
php_fpm_docker_tcp_enabled: true
```

#### php_fpm_docker_listen_addr
IP адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` означает, что будут использоваться все адреса.<br/>
Используется если `php_fpm_docker_tcp_enabled == true`.
```
# default
php_fpm_docker_listen_addr: "0.0.0.0"

# example
php_fpm_docker_listen_addr: "127.0.0.1"
```

#### php_fpm_docker_listen_port
Номер порта, который будет перенаправлен в контейнер.<br/>
Используется если `php_fpm_docker_tcp_enabled == true`.
```
# default
php_fpm_docker_listen_port: 9000
```


## Note
**USR1** - reload logs<br/>
**USR2** - full reload


## Example
### Playbook
```
- name: "Setup PHP-FPM in Docker"
  hosts: locahost
  become: yes
  vars:
    php_fpm_docker_fpm_sock_dir: "/run/{{ php_fpm_docker_container_name }}"
    php_fpm_docker_php_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_docker_instance }}/php"
    php_fpm_docker_fpm_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_docker_instance }}/php-fpm.d"
    php_fpm_docker_extra_volumes:
      - "/var/www:/var/www"
  roles:
    - php_fpm_docker
```
