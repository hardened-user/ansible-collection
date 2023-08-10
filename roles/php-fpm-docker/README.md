# PHP-FPM

Simple installation compatible with the [official Docker image](https://hub.docker.com/_/php)


## Variables
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

#### php_fpm_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
php_fpm_docker_extra_volumes: []

# example
php_fpm_docker_extra_volumes:
  - "/mnt/ram0/php-cache:/var/www/site/html/data/cache"
```

#### php_fpm_tcp_enabled
Разрешить доступ по **TCP/IP**
```
# default
php_fpm_tcp_enabled: true
```

#### php_fpm_listen_addr
**TCP/IP** адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` говорит о том, что будут использоваться все адреса.
```
# default
php_fpm_listen_addr: "0.0.0.0"

# example
php_fpm_listen_addr: "127.0.0.1"
```

#### php_fpm_listen_port
Номер порта, на который будут приниматься подключения.
```
# default
php_fpm_listen_port: 9000
```

#### php_fpm_php_conf_src
Конфигурация **PHP** осуществляется путем копирования файлов из каталога `php_fpm_php_conf_src`.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
php_fpm_php_conf_src: "{{ role_path }}/files/{{ php_fpm_version }}/php"

# example
php_fpm_php_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_version }}/php"
```

#### php_fpm_fpm_conf_src
Конфигурация **FPM** осуществляется путем копирования файлов из каталога `php_fpm_fpm_conf_src`.<br/>
Соответствующие файлы должны быть подготовлены заранее.
```
# default
php_fpm_fpm_conf_src: "{{ role_path }}/files/{{ php_fpm_version }}/php-fpm.d"

# example
php_fpm_fpm_conf_src: "files/php-fpm/{{ inventory_hostname }}/{{ php_fpm_version }}/php-fpm.d"
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
  roles:
    - php-fpm-docker
```
