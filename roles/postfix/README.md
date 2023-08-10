# Postfix MTA
Postfix - агент передачи почты (MTA - mail transfer agent)


## Example
### Variables
Пример настройки на отправку почты через Gmail.
```yaml
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
postfix_file_content_sasl_password_maps: |
  [smtp.gmail.com]:587 login@gmail.com:PaS$w0rD

# http://www.postfix.org/ADDRESS_REWRITING_README.html 
postfix_file_content_smtp_generic_maps: |
  @localhost              server-host@example.com
  @localhost.localdomain  server-host@example.com
  @hostname.lan           server-host@example.com

# Optional
postfix_aliases:
  root: my.mail@gmail.com
  
# Optional for security
postfix_file_content_smtp_header_checks: |
  /^X-Mailer:/                      IGNORE
  /^X-Originating-IP:/              IGNORE
  /^DKIM-Filter:/                   IGNORE
```


### Playbook
```
- name: "Setup Postfix"
  hosts: locahost
  become: yes
  roles:
    - postfix
```
