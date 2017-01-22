#!/usr/bin/python

from tinydb import TinyDB, Query, where
import socket
import sys
import re

db = TinyDB('db.json')   # The database we are storing this in

# we are starting over
db.purge()

for ip in range(51,90):
   ip_addr = '192.168.1.' + str(ip)
   host_info = socket.gethostbyaddr(ip_addr)
   if not re.search('odroid', host_info[0]):
      db.insert({'ip': ip_addr, 'name': host_info[0], 'username':'', 'password':'', 'firstname':'', 'lastname': ''})

# This will find a free VM
#vms = Query()
#print db.search(vms.username == '')

# Show the ones we added
print db.all()
