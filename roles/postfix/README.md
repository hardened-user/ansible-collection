# Postfix MTA

Postfix - агент передачи почты (MTA - mail transfer agent)


## Variables
#### postfix_aliases
Псевдонимы электронной почты в системе.<br/>
См. [man aliases](https://www.postfix.org/aliases.5.html).
```
# default
postfix_aliases: {}

# example
postfix_aliases:
  root: my.mail@gmail.com
```

#### postfix_file_content_smtp_generic_maps
Содержимое файла **smtp_generic_maps**.<br/>
См. [man generic](https://www.postfix.org/generic.5.html).
```
# default
postfix_file_content_smtp_generic_maps: ""

# example
postfix_file_content_smtp_generic_maps: |-
  @localhost              server-host@example.com
  @localhost.localdomain  server-host@example.com
  @hostname.lan           server-host@example.com
```

#### postfix_file_content_sasl_password_maps
Содержимое файла **smtp_sasl_password_maps**.<br/>
См. [man generic](https://www.postfix.org/SASL_README.html).
```
# default
postfix_file_content_sasl_password_maps: ""

# example
postfix_file_content_sasl_password_maps: |-
  [smtp.gmail.com]:587 login@gmail.com:PaS$w0rD
```

#### postfix_file_content_smtp_header_checks
Содержимое файла **smtp_header_checks**.<br/>
См. [man header_checks](https://www.postfix.org/header_checks.5.html).
```
# default
postfix_file_content_smtp_header_checks: ""

# example
postfix_file_content_smtp_header_checks: |-
  /^X-Mailer:/                      IGNORE
  /^X-Originating-IP:/              IGNORE
  /^DKIM-Filter:/                   IGNORE
```

#### postfix_main_conf_dict
Пользовательская конфигурация `main.cf`.<br/>
Перезаписывает `postfix_main_conf_default`, значение `null` удалит переменную.
```
# default
postfix_main_conf_dict: {}
```

#### postfix_main_conf_default
Конфигурация `main.cf` по-умолчанию.
```
# default
postfix_main_conf_default:
  ...
```


## Example
### Playbook
Пример настройки на отправку почты через Gmail.
```
- name: "Setup Postfix MTA"
  hosts: locahost
  become: yes
  vars:
    postfix_main_conf_dict:
      smtp_sasl_auth_enable: "yes"
      smtp_destination_rate_delay: "60s"
      relay_destination_rate_delay: "60s"
      # Optional for OpenDKIM
      #milter_default_action: accept
      #milter_protocol: 2
      #smtpd_milters: unix:/var/run/opendkim/opendkim.sock
      #non_smtpd_milters: $smtpd_milters

    # WARNING !!! Encrypt the content of this variable using Ansible Vault
    # https://docs.ansible.com/ansible/latest/user_guide/vault.html
    postfix_file_content_sasl_password_maps: |-
      [smtp.gmail.com]:587 login@gmail.com:PaS$w0rD

    # http://www.postfix.org/ADDRESS_REWRITING_README.html
    postfix_file_content_smtp_generic_maps: |-
      @localhost              server-host@example.com
      @localhost.localdomain  server-host@example.com
      @hostname.lan           server-host@example.com

    # Optional aliases
    postfix_aliases:
      root: my.mail@gmail.com

    # Optional for security
    postfix_file_content_smtp_header_checks: |-
      /^X-Mailer:/                      IGNORE
      /^X-Originating-IP:/              IGNORE
      /^DKIM-Filter:/                   IGNORE
  roles:
    - postfix
```
