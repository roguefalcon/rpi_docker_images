#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Print users =================================================================
print("==> User")
c.execute('''SELECT * FROM user''')
users = c.fetchall()

for user in users:
        print(user)
