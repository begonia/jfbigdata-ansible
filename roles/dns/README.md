## Example:

inventory:

```
[all]
192.168.1.100
192.168.1.101
192.168.1.102
```

site.yml

```
- name: Set local dns server
  vars:
    # your local dns server, default is 114.114.114.114
    - {"dns_nameservers": ["192.168.1.204", "192.168.1.205"]}
    # interface name, default is only eth0
    - {"interface_name": ["eth0", "eth1"]}
  hosts: all
  remote_user: root

  roles:
    - dns
  tags:
    - test
```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

