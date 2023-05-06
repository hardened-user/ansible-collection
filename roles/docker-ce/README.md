# Docker CE (Community Edition)
https://docs.docker.com/engine/install/

## Example
### Variables
```
# latest
docker_version: ""

# CentOS
docker_version: "20.10.21"

# Ubuntu
docker_version: "5:23.0.5-1~ubuntu.22.04~jammy"
```

```
docker_config_dict:
  storage-driver: "btrfs"
  bip: "172.17.0.1/24"
  default-address-pools:
    - base: "172.18.0.0/15"
      size: 24
  insecure-registries:
    - "self.signed.registry.com"
```

### Playbook
```
- name: "Setup Docker CE"
  hosts: locahost
  become: yes
  roles:
    - docker-ce
```
