#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# List User ==================================================================
print("==> User")
c.execute('''SELECT *
               FROM user''')
data = c.fetchall()

for item in data:
    print(item)

# List Notification =============================================================
print("==> Notification")
c.execute('''SELECT *
               FROM notification''')
data = c.fetchall()
for item in data:
    print(item)

# List Session =============================================================
print("==> Session")
c.execute('''SELECT *
               FROM session''')
data = c.fetchall()

for item in data:
    print(item)

conn.close()
