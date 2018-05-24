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
- name: Set local ntp server
  vars:
    # your local ntp server, default is ntp.sjtu.edu.cn
    - {"ntpserver": "192.168.1.204"}
  hosts: all
  remote_user: root

  roles:
    - ntp
  tags:
    - test
```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

