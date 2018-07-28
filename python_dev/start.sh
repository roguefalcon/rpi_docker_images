#!/bin/bash

service nscd restart
service nslcd restart
/usr/sbin/sshd -D
