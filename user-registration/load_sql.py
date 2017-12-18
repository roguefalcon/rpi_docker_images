#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
c.execute('''CREATE TABLE IF NOT EXISTS vpn_clients
             (username, filename)''')


