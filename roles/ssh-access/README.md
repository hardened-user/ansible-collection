# SSH Access
Роль для добавления / удаления пользователей на хосты

## Конфигурация
Конфигурация разделена на три части:
- пользовательские роли
- активные пользователи
- деактивированные пользователи

### Пользовательские роли
Роли назначаются активным пользователям.
Специальная роль` default` присваивается пользователям для которых роль или группы не задана.
```yaml
ssh_access_user_roles_default:
  - description: "Default groups"
    name: "default"
    user_groups: []
  - description: "Super administrator on all hosts"
    name: "global-super-admin"
    user_groups:
      - sudo
      - wheel
      - docker
  - description: "Database administrator"
    name: "dba"
    user_groups:
      - postgres
    user_hosts:
      - group_db_host
      - pg1.examole.com
```

### Активные пользователи
Пользователи (и их ключи) из этого списка будут добавлены на хосты, к которым у них есть принадлежность.
```yaml
ssh_access_user_enabled_default:
  - description: "Alex King"
    name: "alex.king"
    user_roles:
      - dba
    user_hosts:
      - server.example.com
      - name: host.domain.ru
        user_groups:
          - wheel
      - name: db4.example.com
        enable: false
```

### Деактивированные пользователи
Пользователь и его ключ будут удалены со всех хостов.

NOTE: Так же с хостов удаляются пользователи из группы активных, для которых нет прав на этом хосте.
```yaml
ssh_access_user_disabled:
  - user1
  - user2
```

## Слияние конфигураций
Слияние конфигураций из default роли и заданных при исполнении playbook'a, осуществляется через кастомный фильтр `combine_list_of_dict`, который заменяет или добавляет элементы в первом списке из второго по ключу.
```yaml
ssh_access_user_roles_merged: "{{ ssh_access_user_roles_default|combine_list_of_dict(ssh_access_user_roles, 'name') }}"
ssh_access_user_enabled_merged: "{{ ssh_access_user_enabled_default|combine_list_of_dict(ssh_access_user_enabled, 'name') }}"
ssh_access_user_disabled_merged: "{{ (ssh_access_user_disabled_default + ssh_access_user_disabled) | unique }}"
```

## runtime конфигурация
Под каждый хост во время выполнения playbook'a генерируется `runtime_users_config` через кастомный фильтр `ssh_access_runtime_config`

Приоритеты:
- совпадение с хостом
- совпадение с группой хостов
- совпадение с группой all

```yaml
  runtime_users_config:
    - enable: false
      user_groups: []
      name: alex.king
    - enable: true
      user_groups:
      - wheel
      - sudo
      - docker
      name: pavel.alexeev
    - enable: false
      user_groups: []
      name: ivanov.ivanovich
```

## Конфликты
Пользователь не должен быть одновременно в enabled и disabled группах.

Пользователи и роли не должны дублироваться в одном словаре.
