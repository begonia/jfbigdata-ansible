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
- name: Set local dnsmasq server
  vars:
    # upstream DNS server, default is 114.114.114.114
    - {"dns_upstream1": "192.168.1.204"}
    - {"dns_upstream2": "192.168.1.205"}
  hosts: all
  remote_user: root

  roles:
    - dnsmasq
  tags:
    - test
```

dnsmasq/templates/record.conf.j2

```
address=/test.com/192.168.1.100
address=/a.test.com/192.168.1.101

```

run:

**notice**: you should config __record.conf.j2__ first

```
# ansible-playbook -i inventory -t test site.yml
```


