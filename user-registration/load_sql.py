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

c.execute('''CREATE TABLE vms
             (name text, ip text, username text)''')

# Load the tables =============================================================
#c.execute('''INSERT INTO vpn_users VALUES (?, ?, ?, ?, ?)''', ('asdf', 'asdf@asdf.com', 'asfd', 'asdf', 'asdf.ovpn'))

vms = [
         ('blue.pyatt.lan', '192.168.3.51', ''),
         ('purple.pyatt.lan', '192.168.3.52', ''),
         ('skyblue.pyatt.lan', '192.168.3.53', ''),
         ('green.pyatt.lan', '192.168.3.54', ''),
         ('salmon.pyatt.lan', '192.168.3.55', ''),
         ('pink.pyatt.lan', '192.168.3.56', ''),
         ('periwinkle.pyatt.lan', '192.168.3.57', ''),
         ('teal.pyatt.lan', '192.168.3.58', ''),
         ('grey.pyatt.lan', '192.168.3.59', ''),
         ('mauve.pyatt.lan', '192.168.3.61', ''),
         ('beige.pyatt.lan', '192.168.3.62', ''),
         ('brown.pyatt.lan', '192.168.3.63', ''),
         ('orange.pyatt.lan', '192.168.3.64', ''),
         ('navy.pyatt.lan', '192.168.3.65', ''),
         ('lime.pyatt.lan', '192.168.3.66', ''),
         ('indigo.pyatt.lan', '192.168.3.67', ''),
         ('peach.pyatt.lan', '192.168.3.68', ''),
         ('tan.pyatt.lan', '192.168.3.69', ''),
         ('violet.pyatt.lan', '192.168.3.71', ''),
         ('cyan.pyatt.lan', '192.168.3.72', ''),
         ('maroon.pyatt.lan', '192.168.3.73', ''),
         ('lilac.pyatt.lan', '192.168.3.74', ''),
         ('olive.pyatt.lan', '192.168.3.75', ''),
         ('mustard.pyatt.lan', '192.168.3.76', ''),
         ('black.pyatt.lan', '192.168.3.77', ''),
         ('yellow.pyatt.lan', '192.168.3.78', ''),
         ('red.pyatt.lan', '192.168.3.79', ''),
         ('plum.pyatt.lan', '192.168.3.81', ''),
         ('clay.pyatt.lan', '192.168.3.82', ''),
         ('rose.pyatt.lan', '192.168.3.83', ''),
         ('smoke.pyatt.lan', '192.168.3.84', ''),
         ('taupe.pyatt.lan', '192.168.3.85', ''),
         ('jade.pyatt.lan', '192.168.3.86', ''),
         ('copper.pyatt.lan', '192.168.3.87', ''),
         ('silver.pyatt.lan', '192.168.3.88', ''),
         ('gold.pyatt.lan', '192.168.3.89', '')
      ]
c.executemany('''INSERT INTO vms VALUES (?, ?, ?)''', vms)

conn.commit()
conn.close()
