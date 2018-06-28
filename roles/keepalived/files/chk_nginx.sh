#!/bin/bash

counter=$(ps -C nginx --no-heading|wc -l)

if [ "${counter}" = "0"  ]; then
    nginx
    sleep 2
    counter=$(ps -C nginx --no-heading|wc -l)
    if [ "${counter}" = "0"  ]; then
        systemctl stop keepalived
    fi
fi
