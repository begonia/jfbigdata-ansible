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
- name: Apply common configuration to all nodes
  vars:
    # your subnet yum repo, default is mirrors.ustc.edu.cn
    - {"yum_repo_url": "192.168.1.179"}
  hosts: all
  remote_user: root

  roles:
    - common
  tags:
    - common

```

run:

```
# ansible-playbook -i inventory -t common site.yml
```
