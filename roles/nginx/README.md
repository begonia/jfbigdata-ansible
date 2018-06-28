## Example:

inventory:

```
[all]
192.168.1.100
```

site.yml

```
- name: Config nginx server
  vars:
    # your local yum repo, default is ustc.edu.cn
    - {"yum_repo_url": "192.168.1.179"}
  hosts: all
  remote_user: root

  roles:
    - common
    - nginx
  tags:
    - test
```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

reference:

<https://github.com/geerlingguy/ansible-role-nginx>

