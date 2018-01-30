#!/usr/bin/python3

#Imported libraries
import sqlite3
import bcrypt
import os

#We want to remove the existing file
try:
    os.remove('sql.db')
except OSError as e:
    print("Couldn't remove the file:", e.strerror)

#THe sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

#Make the tables
print('==> activity')
c.execute('''CREATE TABLE IF NOT EXISTS activity
             (todo_id INTEGER, 
              note TEXT,
              status_id INTEGER,
              employee_id INTEGER,
              active INTEGER,
              date_created TEXT)''')

print('==> crew')
c.execute('''CREATE TABLE IF NOT EXISTS crew
             (name TEXT,
              active INTEGER,
              date_created TEXT)''')

print('==> crew member')
c.execute('''CREATE TABLE IF NOT EXISTS crew_member
             (crew_id INTEGER,
              employee_id INTEGER,
              active INTEGER,
              date_created TEXT)''')

print('==> customer')
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

print('==> employee')
c.execute('''CREATE TABLE IF NOT EXISTS employee
             (name TEXT, 
              email TEXT,
              phone TEXT,
              password TEXT,
              message TEXT,
              status_id INTEGER,
              active INTEGER,
              date_created TEXT)''')

print('==> equipment')
c.execute('''CREATE TABLE IF NOT EXISTS equipment
             (name TEXT,
              quantity INTEGER,
              crew_id INTEGER,
              active INTEGER)''')

print('==> notification')
c.execute('''CREATE TABLE IF NOT EXISTS notification
             (type TEXT,
              note TEXT,
              customer_id INTEGER,
              employee_id INTEGER,
              status_id INTEGER,
              active INTEGER,
              date_created TEXT)''')

print('==> schedule')
c.execute('''CREATE TABLE IF NOT EXISTS schedule
             (type TEXT,
              customer_id INTEGER,
              employee_id INTEGER,
              active INTEGER,
              schedule_date TEXT,
              date_created TEXT)''')

print('==> session')
c.execute('''CREATE TABLE IF NOT EXISTS session
             (user_id INTEGER,
              date_created TEXT)''')

print('==> status')
c.execute('''CREATE TABLE IF NOT EXISTS status
             (name TEXT,
              description TEXT,
              status_group TEXT,
              active INTEGER,
              date_created TEXT)''')

print('==> Todo')
c.execute('''CREATE TABLE IF NOT EXISTS todo
             (type TEXT CHECK (type IN ('RFQ', 'Complaint')),
              customer_id INTEGER,
              status_id INTEGER,
              active INTEGER,
              date_created TEXT)''')

print('==> User')
c.execute('''CREATE TABLE IF NOT EXISTS user
             (email TEXT,
              password TEXT,
              employee_id INTEGER,
              customer_id INTEGER,
              status_id INTEGER,
              active INTEGER,
              date_created TEXT)''')


#Let's load some data

activity = [(1, 'hello', 1, 2, 1, '1-27-18')]#6 things
c.executemany('INSERT INTO activity VALUES (?, ?, ?, ?, ?, ?)', activity)


crew = [('Dave', 1, '1-27-18')]#3 things
c.executemany('INSERT INTO crew VALUES(?, ?, ?)', crew)


crew_member = [(3, 2, 1, '1-27-18')]
c.executemany('INSERT INTO crew_member VALUES(?, ?, ?, ?)', crew_member)#4 things


customer = [('John Doe', 'John@joe.com', '1301 E Main Street', 'Madison', 'TN', '37132', '6158982424', 2, 1, '1-27-18')]#10 things
c.executemany('INSERT INTO customer VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', customer)

employee = [('Jason Dupin', 'designer@lawnbots.com', '1111111111', 'awesome27','hello',1 , 1 ,1)]#8 things
c.executemany('INSERT INTO employee VALUES(?, ?, ?, ?, ?, ?, ?, ?)', employee) 

equipment = [('Tool', 10, 5, 1)]#4 things
c.executemany('INSERT INTO equipment VALUES(?, ?, ?, ?)', equipment)

notification = [('mobile','note', 2, 3, 4, 1, '1-27-18')]#7 things
c.executemany('INSERT into notification VALUES(?, ?, ?, ?, ?, ?, ?)', notification)

schedule = [('types', 2, 3, 1, '1-2-34', '1-27-18')]#6 things
c.executemany('INSERT INTO schedule VALUES(?, ?, ?, ?, ?, ?)', schedule)

session = [(3, '1-27-18')]#2 things
c.executemany('INSERT INTO session VALUES(?, ?)', session)

status = [('Filled out RFQ', 'Customer filled out the RFQ', 'Activity', 0, '1-27-18'),
          ('Meeting Scheduled', 'We have scheduled the appointment with the customer', 'Activity', 0, '1-27-18'),
          ('Called', 'Customer has been contacted', 'Activity', 0, '1-27-18'),
          ('Left Message', 'Got the voicemail and left a message', 'Activity', 0, '1-27-18'),
          ('Changed Mind', 'Customer has decided not to use the service', 'Activity', 0, '1-27-18'),
          ('Complaint Processed', 'Customer complaint has been processed', 'Activity', 0, '1-27-18'),
          ('Prospect', 'Customer has requested a quote', 'Customer', 0, '1-27-18'),
          ('Estimate', 'Operations Team has delivered an estimate', 'Customer', 0, '1-27-18'),
          ('Contract', 'Customer has accepted the estimate and signed the contract', 'Customer', 0, '1-27-18'),
          ('Employeed', 'Employee is still working here', 'Employee',0, '1-27-18'),
          ('Fired', 'We mutually decided that it was time for you to leave', 'Employee', 0, '1-27-18'),
          ('Leave', 'Employee has taken a leave of abscense', 'Employee', 0, '1-27-18'),
          ('Queued', 'Message read to be sent', 'Notification', 0, '1-27-18'),
          ('Sent', 'Message has been sent', 'Notification', 0, '1-27-18'),
          ('Read', 'Message has been read by customer', 'Notification', 0, '1-27-18'),
          ('New', 'This Todo has not been looked at yet (read page not visited)', 'Todo', 0, '1-27-18'),
          ('Assigned', 'This Todo is assigned to a CSR', 'Todo', 0, '1-27-18'),
          ('Locked', 'This Todo is locked by a CSR', 'Todo', 0, '1-27-18'),
          ('Completed', 'This Todo is completed', 'Todo', 0, '1-27-18'),
          ('Closed', 'This Todo was closed without work being done', 'Todo', 0, '1-27-18'),
          ('Disabled', 'User account is disabled. User cannot login', 'User', 0, '1-27-18'),
          ('Enabled', 'User account is enabled and can login', 'User', 0, '1-27-18'),
          ('New', 'New account', 'User', 0 ,'1-27-18'),
          ('Admin', 'This account has special privileges', 'User', 0, '1-27-18')]#5 things
c.executemany('INSERT INTO status VALUES(?, ?, ?, ?, ?)', status)

todo = [('RFQ', 4, 2, 0, '1-27-18')]#5 things
c.executemany('INSERT INTO todo VALUES(?, ?, ?, ?, ?)', todo)

user = [('email', bcrypt.hashpw(b'password', bcrypt.gensalt()), 4, 3, 2, 1, '1-27-18')]#7 things
c.executemany('INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?)', user)


conn.commit()


 

