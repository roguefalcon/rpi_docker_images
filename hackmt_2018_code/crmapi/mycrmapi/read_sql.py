#!/usr/bin/python3

#sql library
import sqlite3

#Sql connection & cursor
conn = sqlite3.connect('sql.db')
c=conn.cursor()

#List Customers====================
print("==> Customers")
c.execute('''SELECT rowid,
                    name,
                    email,
                    street,
                    city,
                    state,
                    zip,
                    phone,
                    status_id
                    active
                    date_created
               FROM customer''')
data = c.fetchall()

for item in data:
    print (item)

