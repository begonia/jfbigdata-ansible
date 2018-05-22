##  Example:

inventory:

```
[kibana]
192.168.1.100
```

site.yml

```
- name: deploy kibana                                                           
  hosts: kibana                                                                 
  remote_user: root                                                             
  vars:
    - {"kibana_server": "192.168.1.211"}
    - {"elasticsearch_url": "192.168.1.211"}
  roles:                                                                        
    - kibana                                                                    
  tags:                                                                         
    - kibana 
```

run:

```
# ansible-playbook -i inventory -t kibana site.yml
```
