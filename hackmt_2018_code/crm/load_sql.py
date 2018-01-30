#!/usr/bin/python3

# imported libraries
import sqlite3
import bcrypt
import os

# We want to remove the existing file
try:
        os.remove('sql.db')
except OSError as e:
        print("Couldn't remove the file:", e.strerror)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
c.execute('''CREATE TABLE IF NOT EXISTS employee
            (name text, email text, phone text, password text, message text,
            status_id integer, active integer, date_created text)''')

c.execute('''CREATE TABLE IF NOT EXISTS todo
            (todo_type text, customer_id iteger, status_id integer, 
            active integer, date_created text)''')

c.execute('''CREATE TABLE IF NOT EXISTS activity
            (todo_id integer, note text, status_id integer, employee_id integer,
            active integer, date_created text)''')

c.execute('''CREATE TABLE IF NOT EXISTS status
            (name text, description text, status_group text, active integer,
            date_created text)''')

c.execute('''CREATE TABLE IF NOT EXISTS customer
            (name text, email text, street text, city text, state text, zip text, phone text,
            status_id integer, active integer, date_created text)''')

# employees
c.execute('''INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
         ('Hunter Lightner', 'hunter@MowMyLawn.com', '5555555555', bcrypt.hashpw(b'nowhere', bcrypt.gensalt()), 'Get workin', 10, 1, '1/26/2018'))

c.execute('''INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
         ('I B Winen', 'winner@MowMyLawn.com', '5555556666', bcrypt.hashpw(b'somewhere', bcrypt.gensalt()), 'Lunch', 10, 2, '1/26/2018'))

c.execute('''INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
         ('Seymore Butts', 'butts@MowMyLawn.com', '5555557777', bcrypt.hashpw(b'Behanju', bcrypt .gensalt()), 'NONE', 10, 3, '1/26/2018'))

# todos
c.execute('''INSERT INTO todo VALUES (?, ?, ?, ?, ?)''',
         ('RFQ', 1, 1, 1, '1/27/2018'))

c.execute('''INSERT INTO todo VALUES (?, ?, ?, ?, ?)''',
         ('RFQ', 2, 2, 2, '1/27/2018'))

c.execute('''INSERT INTO todo VALUES (?, ?, ?, ?, ?)''',
         ('Complaint', 2, 2, 2, '1/27/2018'))

# activities
c.execute('''INSERT INTO activity VALUES (?, ?, ?, ?, ?, ?)''',
         (1, 'in progress', 1, 2, 2, '1/27/2018'))

# activity statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Filled out RFQ', 'Customer filled out the RFQ', 'activity statuses', 1, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Meeting Schedual', 'Meeting with customer has been schedualed', 'activity statuses', 2, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Called', 'Customer has been contacted', 'activity statuses', 3, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Left Message', 'Left a voicemail with customer', 'activity statuses', 4, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Changed Mind', 'Customer has decided not to use service', 'activity statuses', 5, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Complaint Preccessed', 'Customer complaint has been proccessed', 'activity statuses', 6, '1/27/2018'))

# customer statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Prospect', 'Customer has requested a qoute', 'cuntomer statuses', 7, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Estimate', 'Operations Team has delivered an estimate', 'cuntomer statuses', 8, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Conract', 'Customer has accepted an estimate and has signed a contract', 'cuntomer statuses', 9, '1/27/2018'))

# Employee Statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Employed', 'Current employee', 'employee statuses', 10, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Fired', 'We mutually decided it was time to let you go', 'employee statuses', 11, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Leave', 'Employee has taken a leave of absence', 'employee statuses', 12, '1/27/2018'))

# Notification Statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Queued', 'Message to be sent', 'notification statuses', 13, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Sent', 'Message has been sent', 'notification statuses', 14, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Read', 'Message has been read by customer', 'notification statuses', 15, '1/27/2018'))

# Todo Statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('New', 'This Todo has not been looked at yet', 'todo statuses', 16, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Assigned', 'This Todo has been assigned to a CSR', 'todo statuses', 17, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Locked', 'This Todo is locked by a CSR', 'todo statuses', 18, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Completed', 'This Todo is comlpete', 'todo statuses', 19, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Closed', 'This Todo was closed without completeing the work', 'todo statuses', 20, '1/27/2018'))

# User Statuses
c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Disabled', 'User account disabled, user can not login', 'user statuses', 21, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Enabled', 'User account enabled, user can login', 'user statuses', 22, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('New', 'New Account', 'user statuses', 23, '1/27/2018'))

c.execute('''INSERT INTO status VALUES (?, ?, ?, ?, ?)''',
         ('Admin', 'This account has special privileges', 'user statuses', 24, '1/27/2018'))

# Customers
c.execute('''INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
         ('John Buck', 'johnB@hotmail.com', 'dust st', 'Undegrund', 'TN', '14345',
          '1234567891', 22, 1, '1/26/2018'))

c.execute('''INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
         ('Jane Doe', 'janeD@hotmail.com', 'flower st', 'Crematoria', 'TN', '18745',
          '1234367891', 22, 1, '1/26/2018'))

c.execute('''INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
         ('Lucy Goosy', 'Lucy@hotmail.com', 'dance st', 'Hermitage', 'TN', '14645',
          '1234564891', 22, 1, '1/26/2018'))

c.execute('''INSERT INTO customer VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
         ('Grand Pa', 'gramps@hotmail.com', 'old st', 'Ancient', 'TN', '14375',
          '1234587891', 22, 1, '1/26/2018'))
         

conn.commit()

