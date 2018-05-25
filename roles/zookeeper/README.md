##  Example:

inventory:

```

[zookeeper]
hp1 myid=1
hp2 myid=2
hp3 myid=3

```

site.yml

```
- name: deploy zookeeper cluster                                                
  hosts: zookeeper                                                              
  remote_user: root                                                             

  roles:                                                                        
    - ntp
    - java
    - zookeeper                                                                 
  tags:                                                                         
    - zookeeper 
```

run:

```
# ansible-playbook -i inventory -t zookeeper site.yml
```
