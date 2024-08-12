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
          PrivateKey: *****
          Address:  10.9.0.3/24
        peer:
          PublicKey: *****
          AllowedIPs: 10.9.0.0/24, 0.0.0.0/0
          Endpoint: wg.server.com:51820
          PersistentKeepalive: 15
      - name: work2
        enabled: false          <----- disabled
        interface:
          PrivateKey: *****
          Address:  192.168.0.10/24
        peer:
          PublicKey: *****
          AllowedIPs: 192.168.0.00/24
          Endpoint: example.com:51820
          PersistentKeepalive: 15
  roles:
    - wireguard_client
```
