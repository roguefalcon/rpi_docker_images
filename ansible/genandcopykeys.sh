#!/bin/bash

ssh-keygen -t rsa -C "root@raspberry3"
ssh-copy-id root@192.168.3.50
ssh-copy-id root@192.168.3.60
ssh-copy-id root@192.168.3.70
ssh-copy-id root@192.168.3.80
