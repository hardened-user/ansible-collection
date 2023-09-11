# Logrotate

Setup default options for `logrotate`.

## Variables
#### logrotate_interval
Как часто производить ротацию.<br/>
Доступные варианты: `hourly`
```
logrotate_interval: "daily"
```

#### logrotate_rotate
Количество архивных файлов, которые будут сохранены.
```
logrotate_rotate: 31
```

#### logrotate_dateext
К имени архивных файлов добавлять дату вместо номера.
```
logrotate_dateext: true
```


## Example
### Playbook
```
- name: "Setup logrotate"
  hosts: locahost
  become: yes
  roles:
    - logrotate
```
