##  Example:

inventory:

```
[all]
192.168.1.100
192.168.1.101
192.168.1.102
```

site.yml

```
- name: Apply linux bridge configuration to all nodes
  vars:
    # your subnet yum repo, default is mirrors.ustc.edu.cn
    - {"yum_repo_url": "192.168.1.179"}
    - {"netmask": "255.255.255.0"}
    - {"gateway": "192.168.1.1"}
    - {"dns": "114.114.114.114"}
    # which interface bridge to br0"
    - {"nic": "em1"}
  hosts: all
  remote_user: root

  roles:
    - common
    - linuxbridge
  tags:
    - linuxbridge

```

run:

```
# ansible-playbook -i inventory -t linuxbridge site.yml
```
