##  Example:

inventory:

```
[all]
es1
es2
es3
```

site.yml

```
- name: Deploy ElasticSearch Cluster
  hosts: all
  remote_user: root

  roles:                                                                        
  - {role: elasticsearch, es_instance_name: "node1", es_heap_sie: "16g",        
    es_config: {                                                                
        cluster.name: "jf-elasticsearch",                                       
        discovery.zen.ping.unicast.hosts: "192.168.1.211:9300,192.168.1.221:9300,192.168.1.231:9300",
        discovery.zen.minimum_master_nodes: 2,                                  
        network.host: "_eth0_",                                                 
        http.port: 9200,                                                        
        transport.tcp.port: 9300,                                               
        node.data: true,                                                        
        node.master: true,                                                      
        bootstrap.memory_lock: false,                                           
     }}                                                                          
  tags:                                                                         
    - elasticsearch   
```

run:

```
# ansible-playbook -i inventory -t elasticserach site.yml
```
