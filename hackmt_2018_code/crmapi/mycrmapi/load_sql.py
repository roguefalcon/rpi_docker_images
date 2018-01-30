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

# List Customers ==============================================================
print("==> Customers")
c.execute('''CREATE TABLE IF NOT EXISTS customer
             (name TEXT,
             email TEXT,
            street TEXT,
              city TEXT,
             state TEXT,
               zip TEXT,
             phone TEXT,
         status_id INTEGER,
            active INTEGER,
      date_created TEXT)''')

# Make the Employees ==========================================================
print("==> Employees")
c.execute('''CREATE TABLE IF NOT EXISTS employee
             (   name TEXT,
                email TEXT,
             password INTEGER,
               active INTEGER)''')

# Let's load some data
employees = [('Jason Dupin', 'designer@lawnbots.com', 'awesome27', 1),
             ('Prakash Patel', 'vpofdev@lawnbots.com', 'hindirocks99', 1),
             ('Kenny Pyatt', 'ceo@lawnbots.com', 'automationisgr8', 1)]
c.executemany('INSERT INTO employee VALUES(?, ?, ?, ?)', employees)

# Now we need to save the changes to the file
conn.commit()
