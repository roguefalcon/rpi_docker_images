#!/usr/bin/python3

# Imported libraries
import sqlite3
import os, errno

# Remove the database file (we want to start fresh)
try:
   os.remove('sql.db')
except OSError as e:
   if e.errno != errno.ENOENT:
      print("Couldn't drop sql.db:", e)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
c.execute('''CREATE TABLE vpn_users
             (name text, email text, username text, password text, filename text)''')

c.execute('''INSERT INTO vpn_users VALUES (?, ?, ?, ?, ?)''', ('asdf', 'asdf@asdf.com', 'asfd', 'asdf', 'asdf.ovpn'))

conn.commit()
conn.close()
