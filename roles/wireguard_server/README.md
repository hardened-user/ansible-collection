# WireGuard Server

WireGuard VPN Server configration

## Example
### Playbook
```
- name: "Setup WireGuard VPN Server"
  hosts: locahost
  become: yes
  vars:
    wireguard_server_network_address: "10.9.0.1/24"
    wireguard_server_clients:
     - name: client1
       key: *****           <----- client public key
       ip: 10.9.0.5
  roles:
    - wireguard_server
```
