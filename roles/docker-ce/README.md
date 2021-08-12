Docker CE (Community Edition)
================

https://docs.docker.com/engine/install/


Example
==============
```
docker_config_keys:
  storage-driver: "btrfs"
  bip: "172.17.0.1/24"
  default-address-pools:
    - base: "172.18.0.0/15"
      size: 24
  insecure-registries:
    - "self.signed.registry.com"
```
