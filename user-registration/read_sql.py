#!/usr/bin/python3

# Imported libraries
import sqlite3
import os, errno
#import texttable as tt

# The sql connection & cursor
conn = sqlite3.connect('sql.db', check_same_thread=False)
c = conn.cursor()

print("==> Users ==============================================================")
c.execute('''SELECT * from vpn_users''')
for i in c.fetchall():
   print(i)

print("\n==> Virtual Servers (assigned) =========================================")
c.execute('''SELECT * from vms WHERE username != ""''')
for i in c.fetchall():
   print(i)

print("\n==> Virtual Servers (free) =============================================")
c.execute('''SELECT * from vms''')
for i in c.fetchall():
   print(i[0])
