# Zabbix Server with PostgreSQL database support

Simple installation compatible with the [official Docker image](https://hub.docker.com/r/zabbix/zabbix-server-pgsql)


## Variables
#### zabbix_server_pgsql_version
Версия **Zabbix Server**.<br/>
Используется как базовое значение для определения других переменных, имён каталогов и т.п.
```
# default
zabbix_server_pgsql_version: "7.0"
```

#### zabbix_server_pgsql_docker_uid
**UID** пользователя, под которым работает приложение внутри контейнера.
```
# default
zabbix_server_pgsql_docker_uid: 1997
```

#### zabbix_server_pgsql_docker_gid
**GID** пользователя, под которым работает приложение внутри контейнера.
```
# default
zabbix_server_pgsql_docker_gid: 1995
```

#### zabbix_server_pgsql_docker_network
Параметр указывает, в каком сетевом пространстве будет запущен docker контейнер.<br/>
Доступные варианты [bridge](https://docs.docker.com/network/drivers/bridge/) или [host](https://docs.docker.com/network/drivers/host/).
```
# default
zabbix_server_pgsql_docker_network: bridge
```

#### zabbix_server_pgsql_docker_bind_mount_volumes
Параметр указывает, где будут храниться данные:<br/>
* `true` - данные будут храниться в каталоге на хосте.<br/>
* `false` - данные будут храниться в docker volume.
```
# default
zabbix_server_pgsql_docker_bind_mount_volumes: true
```

#### zabbix_server_pgsql_docker_extra_volumes
Дополнительные каталоги для монтирования в контейнер.
```
# default
zabbix_server_pgsql_docker_extra_volumes: []
```

#### zabbix_server_pgsql_docker_export_dir
Каталог для хранения данных [real_time_export](https://www.zabbix.com/documentation/6.0/en/manual/appendix/install/real_time_export) на диске.<br/>
Используется если `zabbix_server_pgsql_docker_bind_mount_volumes: false`
```
# default
zabbix_server_pgsql_docker_export_dir: "{{ zabbix_server_pgsql_docker_compose_dir }}/export"
```

#### zabbix_server_pgsql_docker_snmptraps_dir
Каталог для хранения данных [snmptrap](https://www.zabbix.com/documentation/6.0/en/manual/config/items/itemtypes/snmptrap) на диске.<br/>
Используется если `zabbix_server_pgsql_docker_bind_mount_volumes: false`
```
# default
zabbix_server_pgsql_docker_snmptraps_dir: "{{ zabbix_server_pgsql_docker_compose_dir }}/snmptraps"
```

#### zabbix_server_pgsql_docker_alertscripts_src
Каталог, откуда будут скопированы пользовательские скрипты [Custom alert scripts](https://www.zabbix.com/documentation/6.0/en/manual/config/notifications/media/script).
```
# default
zabbix_server_pgsql_docker_alertscripts_src: "{{ role_path }}/files/alertscripts"

# example
zabbix_server_pgsql_docker_alertscripts_src: "files/zabbix-server-pgsql/{{ inventory_hostname }}/alertscripts"
```

#### zabbix_server_pgsql_docker_externalscripts_src
Каталог, откуда будут скопированы пользовательские скрипты [External checks](https://www.zabbix.com/documentation/6.0/en/manual/config/items/itemtypes/external).
```
# default
zabbix_server_pgsql_docker_externalscripts_src: "{{ role_path }}/files/externalscripts"

# example
zabbix_server_pgsql_docker_externalscripts_src: "files/zabbix-server-pgsql/{{ inventory_hostname }}/externalscripts"
```

#### zabbix_server_pgsql_docker_listen_addr
IP адрес, на который будут приниматься подключения.<br/>
Специальная запись `0.0.0.0` означает, что будут использоваться все адреса.
```
# default
zabbix_server_pgsql_docker_listen_addr: "0.0.0.0"

# example
zabbix_server_pgsql_docker_listen_addr: "127.0.0.1"
```

#### zabbix_server_pgsql_docker_listen_port
Номер порта, который будет перенаправлен в контейнер.
```
# default
zabbix_server_pgsql_docker_listen_port: 10051
```

#### zabbix_server_pgsql_docker_environment
Переменные окружения docker контейнера.
```
# default
zabbix_server_pgsql_docker_environment: {}

# example
zabbix_server_pgsql_docker_environment:
  POSTGRES_PASSWORD: "Pas$w0rd"
  ZBX_TIMEOUT: 5
```


## Note
Список переменных окружения поддерживаемых в `docker-entrypoint.sh`:
```
ZBX_ALLOWUNSUPPORTEDDBVERSIONS - AllowUnsupportedDBVersions
ZBX_CACHESIZE - CacheSize
ZBX_CACHEUPDATEFREQUENCY - CacheUpdateFrequency
ZBX_DBTLSCAFILE - DBTLSCAFile
ZBX_DBTLSCERTFILE - DBTLSCertFile
ZBX_DBTLSCIPHER - DBTLSCipher
ZBX_DBTLSCIPHER13 - DBTLSCipher13
ZBX_DBTLSCONNECT - DBTLSConnect
ZBX_DBTLSKEYFILE - DBTLSKeyFile
ZBX_DEBUGLEVEL - DebugLevel
ZBX_EXPORTFILESIZE - ExportFileSize
ZBX_EXPORTTYPE - ExportType
ZBX_HANODENAME - HANodeName
ZBX_HISTORYCACHESIZE - HistoryCacheSize
ZBX_HISTORYINDEXCACHESIZE - HistoryIndexCacheSize
ZBX_HISTORYSTORAGEDATEINDEX - HistoryStorageDateIndex
ZBX_HISTORYSTORAGETYPES - HistoryStorageTypes
ZBX_HISTORYSTORAGEURL - HistoryStorageURL
ZBX_HOUSEKEEPINGFREQUENCY - HousekeepingFrequency
ZBX_IPMIPOLLERS - StartIPMIPollers
ZBX_JAVAGATEWAY - JavaGateway
ZBX_JAVAGATEWAYPORT - JavaGatewayPort
ZBX_LISTENBACKLOG - ListenBacklog
ZBX_LOGSLOWQUERIES - LogSlowQueries
ZBX_MAXHOUSEKEEPERDELETE - MaxHousekeeperDelete
ZBX_NODEADDRESS - NodeAddress
ZBX_PROBLEMHOUSEKEEPINGFREQUENCY - ServiceManagerSyncFrequency
ZBX_PROXYCONFIGFREQUENCY - ProxyConfigFrequency
ZBX_PROXYDATAFREQUENCY - ProxyDataFrequency
ZBX_SERVICEMANAGERSYNCFREQUENCY - ServiceManagerSyncFrequency
ZBX_SOURCEIP - SourceIP
ZBX_STARTALERTERS - StartAlerters
ZBX_STARTDBSYNCERS - StartDBSyncers
ZBX_STARTDISCOVERERS - StartDiscoverers
ZBX_STARTESCALATORS - StartEscalators
ZBX_STARTHISTORYPOLLERS - StartHistoryPollers
ZBX_STARTHTTPPOLLERS - StartHTTPPollers
ZBX_STARTJAVAPOLLERS - StartJavaPollers
ZBX_STARTLLDPROCESSORS - StartLLDProcessors
ZBX_STARTODBCPOLLERS - StartODBCPollers
ZBX_STARTPINGERS - StartPingers
ZBX_STARTPOLLERS - StartPollers
ZBX_STARTPOLLERSUNREACHABLE - StartPollersUnreachable
ZBX_STARTPREPROCESSORS - StartPreprocessors
ZBX_STARTPROXYPOLLERS - StartProxyPollers
ZBX_STARTREPORTWRITERS - StartReportWriters
ZBX_STARTTIMERS - StartTimers
ZBX_STARTTIMERS - StartTimers
ZBX_STARTTRAPPERS - StartTrappers
ZBX_STARTVMWARECOLLECTORS - StartVMwareCollectors
ZBX_STATSALLOWEDIP - StatsAllowedIP
ZBX_TIMEOUT - Timeout
ZBX_TLSCAFILE - TLSCAFile
ZBX_TLSCERTFILE - TLSCertFile
ZBX_TLSCIPHERALL - TLSCipherAll
ZBX_TLSCIPHERALL13 - TLSCipherAll13
ZBX_TLSCIPHERCERT - TLSCipherCert
ZBX_TLSCIPHERCERT13 - TLSCipherCert13
ZBX_TLSCIPHERPSK - TLSCipherPSK
ZBX_TLSCIPHERPSK13 - TLSCipherPSK13
ZBX_TLSCRLFILE - TLSCRLFile
ZBX_TLSKEYFILE - TLSKeyFile
ZBX_TLSPSKFILE - TLSPSKFile
ZBX_TLSPSKIDENTITY - TLSPSKIdentity
ZBX_TRAPPERTIMEOUT - TrapperTimeout
ZBX_TRENDCACHESIZE - TrendCacheSize
ZBX_TRENDFUNCTIONCACHESIZE - TrendFunctionCacheSize
ZBX_UNAVAILABLEDELAY - UnavailableDelay
ZBX_UNREACHABLEDELAY - UnreachableDelay
ZBX_UNREACHABLEPERIOD - UnreachablePeriod
ZBX_VALUECACHESIZE - ValueCacheSize
ZBX_VAULTDBPATH - VaultDBPath
ZBX_VAULTURL - VaultURL
ZBX_VMWARECACHESIZE - VMwareCacheSize
ZBX_VMWAREFREQUENCY - VMwareFrequency
ZBX_VMWAREPERFFREQUENCY - VMwarePerfFrequency
ZBX_VMWARETIMEOUT - VMwareTimeout
ZBX_WEBSERVICEURL - WebServiceURL
```


## Example
### Playbook
```
- name: "Setup Zabbix Server in Docker"
  hosts: locahost
  become: yes
  vars:
    zabbix_server_pgsql_docker_environment:
      POSTGRES_PASSWORD: "Pas$w0rd"
      ZBX_TIMEOUT: 5
  roles:
    - zabbix_server_pgsql_docker
```
