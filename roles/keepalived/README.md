This ansible keepalived is only used for nginx HA.

Already enabled nginx process check script at **files/chk_nginx.**

## Example:

inventory:

```
[all]
192.168.1.100
192.168.1.101
```

site.yml

```
- name: Config nginx server HA with keepalived
  vars:
    # your local yum repo, default is ustc.edu.cn
    - {"yum_repo_url": "192.168.1.179"}
    # which interface vip bind to
    - {"keepalived_interface": "eth0"}
    # vip
    - {"keepalived_vip": "192.168.1.98/24"}
  hosts: all
  remote_user: root

  roles:
    - common
    - nginx
    - keepalived
  tags:
    - test
```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

reference:

<https://github.com/evrardjp/ansible-keepalived>
