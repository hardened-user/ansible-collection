# hosts
Setup local DNS using the `/etc/hosts` file.

## Example Playbook
```
- name: "Example"
  hosts: locahost
  become: yes
  vars:
    hosts_config_keys:
      10.16.28.74: postgres postgres.domain.local
  roles:
    - hosts
```
