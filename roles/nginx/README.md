# Nginx
Установка вэб-сервера `nginx`.

Конфигурация осуществляется путем копирования файлов из каталога `nginx_conf_source_dir`.<br/>
Соответствующие файлы должны быть подготовлены заранее (см. [конфиг по-умолчанию](files/conf)).

## Example
#### nginx_user_extra_groups
Имя или список групп, в которые будет добавлен пользователь `{{ nginx_user_name }}`.
```
nginx_user_extra_groups: []
```

### Playbook
```
- name: "Setup Nginx"
  hosts: locahost
  become: yes
  vars:
    nginx_conf_source_dir: "files/nginx/{{ inventory_hostname }}/conf"
  roles:
    - nginx
```
