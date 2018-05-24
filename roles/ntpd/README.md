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
- name: Config local ntpd server
  vars:
    # your ntpd subnet, default is 192.168.1.0
    - {"ntp_subnet": "192.168.100.0"}
    # your ntpd subnet mask, defualt is 255.255.255.0
    - {"ntp_netmask": "255.255.255.0"}
    # your ntpd upstream, default is localhost
    - {"ntp_upstream", "210.72.145.44"}
  hosts: all
  remote_user: root

  roles:
    - common
    - ntpd
  tags:
    - test
```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

