#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# print Todo  ========================================================
print("==> Todos")
c.execute('''SELECT t.type, c.name, c.street, c.city,
        c.state, c.zip, c.phone
        FROM todo t, customer c
        WHERE t.customer_id = c.rowid''')
todos = c.fetchall()

for todo  in todos:
    print(todo)

# Print Employees =================================================================
print("==> Employees")
c.execute('''SELECT * FROM employee''')
employees = c.fetchall()

for employee in employees:
    print(employee)

# Print Activity  =================================================================
print("==> Activities")
c.execute('''SELECT * FROM activity''')
activities = c.fetchall()

for activity in activities:
    print(activity)

# Print Customers  =================================================================
print("==> Customers")
c.execute('''SELECT * FROM customer''')
customers = c.fetchall()

for customer in customers:
    print(customer)

# Print Statuses  =================================================================
print("==> Statuses")
c.execute('''SELECT * FROM status''')
statuses = c.fetchall()

for status in statuses:
    print(status)
