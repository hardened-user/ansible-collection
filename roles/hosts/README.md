# hosts

Setup local DNS using the `/etc/hosts` file.

## Example
### Playbook
```
- name: "Setup local DNS"
  hosts: localhost
  become: yes
  vars:
    hosts_config:
      10.16.28.74: postgres postgres.domain.local
  roles:
    - hosts
```
