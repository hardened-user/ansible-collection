# OpenSearch

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/opensearchproject/opensearch-dashboards)


## Variables
#### opensearch_dashboards_version
Версия **opensearch**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
opensearch_dashboards_version: "2.19.3"
```

#### opensearch_dashboards_docker_instance
Имя экземпляра **opensearch**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
opensearch_dashboards_docker_instance: ""

# example
opensearch_dashboards_docker_instance: "{{ opensearch_dashboards_version.split('.')[:2] | join('.') }}"
```

#### opensearch_dashboards_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
opensearch_dashboards_docker_network: bridge
```

#### opensearch_dashboards_opensearch_hosts
Список адресов **opensearch** для подключения.<br/>
В идеале указать все ноды или несколько, но минимум одна, все остальные ноды кластера узнает автоматически.
```
# default
opensearch_dashboards_opensearch_hosts: ["http://localhost:9200"]
```

#### opensearch_dashboards_docker_environment
Произвольная конфигурация `opensearch.yml`.<br/>
Параметры, через переменные окружения, подставляются скриптом `opensearch-docker-entrypoint.sh` в аргументы командной строки.
```
# default
opensearch_dashboards_docker_environment: {}
```


## Example
### Playbook
```
- name: "Setup OpenSearch in Docker"
  hosts: locahost
  become: yes
  roles:
    - opensearch-docker
```
