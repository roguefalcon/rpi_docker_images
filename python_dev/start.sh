#!/bin/bash

service nscd restart
service nslcd restart

openvpn --daemon --config ovpnfile.ovpn
sleep 25
/usr/sbin/sshd -D
