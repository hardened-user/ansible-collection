# Systemd

Роль для управления конфигурационными файлами системных компонентов `systemd`.


## Variables
#### systemd_system_config
Настройка параметров менеджера системных служб `systemd`.
```
# default
systemd_system_config: []

# example
systemd_system_config:
  - { section: "Manager", option: "DefaultTimeoutStopSec", value: "5min" }
  - { section: "Manager", option: "DefaultDeviceTimeoutSec", value: "30s" }
```

#### systemd_logind_config
Настройка сервиса `systemd-logind`.
```
# default
systemd_logind_config: []

# example
systemd_logind_config:
  - { section: "Login", option: "HandlePowerKey", value: "ignore" }
```

#### systemd_resolved_config
Настройка сервиса `systemd-resolved`.
```
# default
systemd_resolved_config: []

# example
systemd_resolved_config:
  - { section: "Resolve", option: "MulticastDNS", value: "no" }
  - { section: "Resolve", option: "LLMNR", value: "no" }
  - { section: "Resolve", option: "Cache", value: "no-negative" }
```

#### systemd_journald_config
Настройка сервиса `systemd-journald`.
```
# default
systemd_journald_config: []

# example
systemd_journald_config:
  - { section: "Journal", option: "SystemMaxUse", value: "1G" }
```


## Example
### Playbook
```
- name: "Setup Systemd"
  hosts: locahost
  become: yes
  roles:
    - systemd
```
