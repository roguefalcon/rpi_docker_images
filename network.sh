#!/bin/bash

# Let wlan1 talk via wlan0
iptables -A FORWARD -i wlan0 -o wlan1 -j ACCEPT
iptables -A FORWARD -i wlan1 -o wlan0 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE

# Let wlan1 talk via eth0
#iptables -A FORWARD -i eth0 -o wlan1 -j ACCEPT
#iptables -A FORWARD -i wlan1 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -i wlan1 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan1 -m state --state ESTABLISHED,RELATED -j ACCEPT
