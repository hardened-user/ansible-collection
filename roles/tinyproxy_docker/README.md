# tinyproxy - a light-weight HTTP/HTTPS proxy daemon for POSIX operating systems

Simple installation compatible with the [hardeneduser/tinyproxy](https://hub.docker.com/r/hardeneduser/tinyproxy)


## Variables
#### tinyproxy_docker_version
Version of **tinyproxy**.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
tinyproxy_docker_version: "latest"
```

#### tinyproxy_docker_tag
Explicit docker tag.<br/>
```
# default
tinyproxy_docker_tag: "{{ tinyproxy_docker_version }}"
```

#### tinyproxy_docker_instance
Instance name of **tinyproxy**.<br/>
Used as a base value for defining other variables, directory names, etc.
```
# default
tinyproxy_docker_instance: ""
```

#### tinyproxy_docker_compose_extra_conf
Additional parameters for the service in **docker-compose**.
```
# default
tinyproxy_docker_compose_extra_conf: {}

# example
tinyproxy_docker_compose_extra_conf:
  deploy:
    resources:
      limits:
        cpus: "1"
        memory: "512M"
      reservations:
        memory: "64M"
  logging:
    driver: "json-file"
    options:
      max-size: "8m"
```

#### tinyproxy_docker_extra_volumes
Additional directories to mount into the container.
```
# default
tinyproxy_docker_extra_volumes: []
```

#### tinyproxy_docker_listen_addr
IP address for accepting incoming connections.<br/>
The value `0.0.0.0` means all available addresses.
```
# default
tinyproxy_docker_listen_addr: "0.0.0.0"
```

#### tinyproxy_docker_listen_port
Port number that will be used by the container for incoming connections.
```
# default
tinyproxy_docker_listen_port: 8888
```

#### tinyproxy_docker_environment
Custom environment variables configuration.<br/>
Overrides `tinyproxy_docker_env_default`, the value `null` will remove the variable.
```
# default
tinyproxy_docker_environment: {}
```

#### tinyproxy_docker_env_default
Default environment variables.
```
# default
tinyproxy_docker_env_default:
  TINYPROXY_LISTEN: "{{ tinyproxy_docker_listen_addr }}"
  TINYPROXY_PORT: "{{ tinyproxy_docker_listen_port }}"
```


## Example
### Playbook
```
- name: "Setup tinyproxy in Docker"
  hosts: localhost
  become: yes
  vars:
    tinyproxy_docker_environment:
      TINYPROXY_ALLOW: "0.0.0.0/0, ::/0"
      TINYPROXY_BASICAUTH_USER: "user"
      TINYPROXY_BASICAUTH_PASS: "pass"
  roles:
    - tinyproxy_docker
```
