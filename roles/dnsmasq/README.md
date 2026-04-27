# Dnsmasq


## Variables
#### dnsmasq_config
```
# default
dnsmasq_config: {}

# example
dnsmasq_config:
  except-interface: "lo"
  bind-dynamic: true
```


## Example
### Playbook
```
- name: "Setup Dnsmasq"
  hosts: locahost
  become: yes
  roles:
    - dnsmasq
```
