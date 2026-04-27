# Dnsmasq

This playbook automates the deployment and configuration of `dnsmasq`.


## Variables
#### dnsmasq_config
```
# default
dnsmasq_config: {}

# example
dnsmasq_config:
  except-interface: "lo"
  bind-dynamic: true
  server:
    - "8.8.8.8"
    - "1.1.1.1"
```

#### dnsmasq_dhcp_hosts
```
# default
dnsmasq_dhcp_hosts: []

# example
dnsmasq_dhcp_hosts:
  - { name: host01, ipv4: 192.168.0.101, mac: 54-6A-69-30-AA-B7 }
  - { name: host02, ipv4: 192.168.0.102, mac: 34:F4:03:06:A1:D4 }
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
