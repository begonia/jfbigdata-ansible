#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import commands
import fcntl
import json
import os
import sys
import socket
import struct


cpu = "cat /proc/cpuinfo | grep name | cut -f2 -d ':' | uniq"
cpu_cores = "cat /proc/cpuinfo |grep cores | cut -d ':' -f2 | uniq"
mem = "cat /proc/meminfo |grep MemTotal |cut -f2 -d : |awk '{a=int($1/1024/1024+1);b=\"G\";c=(a\"\"b);print c}'"
#men_num = "dmidecode|grep -P -A5 'Memory\s+Device'|grep Size|grep -v Range |grep -v 'No Module Installed' |wc -l"
parttions = "cat /proc/partitions |egrep \"[sv]d[a-z]{1}$|xvd[a-z]{1}$\" |awk '{a=int($3/1024/1024);b=\"G\";c=(a\"\"b);print $4,c}'"
#mun_partitions = "cat /proc/partitions |egrep \"[sv]d[a-z]{1}$|xvd[a-z]{1}$\" |wc -l"
uname = "uname -a"
bit = "getconf LONG_BIT"
kernel = "cat /proc/version  |awk '{print $3}'"
uptime = "cat /proc/uptime | awk '{print $1}'"
#network = "lspci | grep Ethernet |cut -f3 -d :"


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_cpu_info():
    return {"info": command(cpu),
            "cores": command(cpu_cores)}

def get_memory_info():
    return {"size": command(mem)}

def get_disk_info():
    disk = []
    for i in command(parttions).split('\n'):
        device, size = i.split(' ')
        disk.append({"devicename": device, "size": size})
    return disk
        
def get_ip_info():
    network_script_path = "/etc/sysconfig/network-scripts/"
    eth_info = []

    ifcfg_list=os.listdir(network_script_path)
    for ifcfg in ifcfg_list:
        if ifcfg.startswith("ifcfg") and not ifcfg.find("lo") != -1 and not ifcfg.find("~") != -1:
            key = ifcfg.split("-")[-1].strip()
            line_list = open(network_script_path + ifcfg).readlines()
            ip = ""
            for line in  line_list:
                if line.startswith("IPADDR"):
                    ip = line.split("=")[-1].strip().strip('"')
            eth_info.append({"ifname": key, "ip": ip})
    return eth_info

def get_sys_info():
    return {"uname": command(uname),
            "bit": command(bit),
            "kernel": command(kernel),
            "uptime": command(uptime)}

def command(comm):
    (status, output) = commands.getstatusoutput(comm)
    return output.lstrip()

def info():
    return {"cup": get_cpu_info(),
            "memory": get_memory_info(),
            "disk": get_disk_info(),
            "ip": get_ip_info(),
            "system": get_sys_info()}

if __name__=="__main__":
    #ifname ="wlp4s0"
    #print get_ip_address(ifname)
    print json.dumps(info())

