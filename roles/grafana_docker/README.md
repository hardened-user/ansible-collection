# Grafana

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/grafana/grafana)


## Variables
#### grafana_docker_version
Version of **Grafana**.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
grafana_docker_version: "12.4.3"
```

#### grafana_docker_instance
Instance name.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
grafana_docker_instance: ""
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
