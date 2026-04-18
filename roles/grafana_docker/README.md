# Grafana

Simple installation **Grafana** with the [official Docker image](https://hub.docker.com/r/grafana/grafana/)


## Variables
#### vm_single_version
Version of **Grafana**.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
vm_single_version: "1.140.0"
```

#### vm_single_docker_instance
Instance name.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
vm_single_docker_instance: ""
```


## Example
### Playbook
```
- name: "Setup Grafana in Docker"
  hosts: locahost
  become: yes
  roles:
    - grafana_docker
```
