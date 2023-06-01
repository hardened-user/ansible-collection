# PHP-FPM
Simple installation compatible with the [official Docker image](https://hub.docker.com/_/php)


## NOTE
**USR1** - reload logs<br/>
**USR2** - full reload


## Example
### Variables
```
php_fpm_php_conf_source: "files/php-fpm-docker/{{ inventory_hostname }}/{{ php_fpm_version }}/php"
php_fpm_fpm_conf_source: "files/php-fpm-docker/{{ inventory_hostname }}/{{ php_fpm_version }}/php-fpm.d"
```


### Playbook
```
- name: "Setup PHP-FPM in Docker"
  hosts: locahost
  become: yes
  roles:
    - php-fpm-docker
```
