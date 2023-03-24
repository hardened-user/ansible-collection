# etcd
Setup `etcd` standalone or multi-member cluster.

**!!! USE ONLY FOR INITIAL INSTALLATION OR UPDATE PROPERTIES !!!**.<br />
Adding or removing nodes to the cluster is not supported correctly.

## Example
### Inventory
`etcd_node_address` - individual address value for each host

```
etcd_nodes:
  hosts:
    node01:
    node02:
    node03:
  vars:
    etcd_node_address: "{{ ansible_default_ipv4.address }}"
```

### Playbook
```
- name: "Install etcd"
  hosts: etcd_nodes
  become: yes
  roles:
    - etcd-v3
```
