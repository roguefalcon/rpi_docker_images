#!/usr/bin/python3

# Imported libraries
import sqlite3
import os, errno

# The sql connection & cursor
conn = sqlite3.connect('sql.db', check_same_thread=False)
c = conn.cursor()

c.execute('''SELECT * from vpn_users''')

for i in c.fetchall():
   print(i)
