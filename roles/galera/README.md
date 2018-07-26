## Example:

inventory:

```
[galera_all]
192.168.140.42 ansible_host=192.168.140.42 ansible_user=root ansible_password=Zhgsmjy12#$ ansible_become=true 
192.168.140.43 ansible_host=192.168.140.43 ansible_user=root ansible_password=Zhgsmjy12#$ ansible_become=true 
192.168.140.44 ansible_host=192.168.140.44 ansible_user=root ansible_password=Zhgsmjy12#$ ansible_become=true
```

`ansible_host`必须写前面


site.yml

```
- name: Set Galera Cluster
  hosts: galera_all
  vars:
    - {"yum_repo_url": "192.168.140.179"}
    - {"ntpserver": "192.168.140.204"}
  remote_user: root

  roles:
    - common
    - ntp
    - galera
  tags:
    - test

```

run:

```
# ansible-playbook -i inventory -t test site.yml
```

galera_wsrep_sst_method: mysqldump
可修改为xtrabackup-v2, 该选项需要安装peronca包


