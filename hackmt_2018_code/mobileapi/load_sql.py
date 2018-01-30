#!/usr/bin/python3

# Imported libraries
import sqlite3
import os

# We want to remove the existing file
try:
    os.remove('sql.db')
except OSError as e:
    print("Couldn't remove the file:", e.strerror)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

print("Processing tables")

# Make the User ==========================================================
print("==> Notification")
c.execute('''CREATE TABLE IF NOT EXISTS notification
             (  type	text,
                note	text,
                customer_id	integer,
                employee_id	integer,
                status_id	integer,
                active	integer,
                date_created    text)''')

print("==> User")
c.execute('''CREATE TABLE IF NOT EXISTS user
             (  email	text,
                password	text,
                employee_id	integer,
                customer_id	integer,
                status_id	integer,
                active	integer,
                date_created	text)''')

print("==> Session")
c.execute('''CREATE TABLE IF NOT EXISTS session
             (  user_id	integer,
                date_created	text)''')


c.execute('''
                INSERT INTO notification
                     VALUES ('Service', 'Praksh requested mow service',1,1,1,1,'01/01/2017')
              ''')

c.execute('''
              INSERT INTO notification
                   VALUES ('Service', 'Kenny requested mow service',1,1,1,1,'01/01/2017')
            ''')

c.execute('''
              INSERT INTO notification
                   VALUES ('Service', 'Neel requested mow service',1,1,1,1,'01/01/2017')
            ''')

# Now we need to save the changes to the file
conn.commit()
