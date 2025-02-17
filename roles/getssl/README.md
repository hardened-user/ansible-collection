# GetSSL

[getssl](https://github.com/srvrco/getssl/) - Obtain SSL certificates from the letsencrypt.org ACME server.

Роль устанавливает скрипт `getssl `и производит настройку.

При первом запуске, будут сгенерированы самоподписанные сертификаты.<br/>
Это поможет решить проблему, когда следом разворачивается web-сервер с готовой конфигурацией **HTTPS**.<br/>
В этом случае файл сертификата уже должен существовать перед запуском, в противном случае будет ошибка при старте.<br/>
А для получения сертификата **Let's Encrypt** потребуется рабочий web-сервер.<br/>
В этом случае, при старте будут использованы самоподписанные сертификаты,<br/>
а затем можно повторно запустить роль или выполнить команду:
```
sudo su - getssl
~/bin/getssl -a
```


## Variables
#### getssl_production_enabled
**Let's Encrypt** устанавливает лимит на количество обращений на генерацию сертификата, поэтому для начала предлагается использовать тестовый сервис.<br/>
После проверки работоспособности конфигурации и процедуры получения сертификатов, нужно переключить в **production** режим.
```
getssl_production_enabled: false
```

#### getssl_renewal_period
Количество дней, оставшихся до окончания срока действия сертификата, в этот период **getssl** будет обновлять сертификат.<br/>
Т.е. будет 30 дней на обновление.
```
getssl_renewal_period: 30
```


## Example
### Playbook
```
- name: "Setup GetSSL"
  hosts: locahost
  become: yes
  vars:
    getssl_production_enabled: true
    getssl_domain_list:
      - { 'name': "example.com" }
      - { 'name': "example.ru", 'sans': ["www.example.ru"] }
  roles:
    - getssl
```
