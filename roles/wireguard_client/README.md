# WireGuard Client

WireGuard VPN Client configration


## Example
### Playbook
```
- name: "Setup WireGuard VPN Client"
  hosts: locahost
  become: yes
  vars:
    wireguard_client_tunnels:
      - name: work
        interface:
          PrivateKey: 0NHEAP9DibhgOp9fCCA3RFf1CR17PLCnbv8Srt071lo=
          Address:  10.9.0.3/24
        peer:
          PublicKey: oA8lsp4gklV6GSuut8X6u5wQIDlahOKuEpVPqWyzfXg=
          AllowedIPs: 10.9.0.0/24, 0.0.0.0/0
          Endpoint: wg.server.com:51820
          PersistentKeepalive: 15
  roles:
    - wireguard_client
```
