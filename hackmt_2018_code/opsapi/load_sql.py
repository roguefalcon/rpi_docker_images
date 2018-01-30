#!/usr/bin/python3

# import libraries
import sqlite3
import os

#removing existing files
try:
	os.remove('sql.db')
except OSError as e:
	print("Couldn't remove the file:", e.strerror)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

print("Processing tables")

# Make the crew table
print("==> Activity")
c.execute('''CREATE TABLE IF NOT EXISTS activity
			(	todo_id INTEGER,
				note	TEXT,
				statue_id INTEGER,
				employee_id INTEGER,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO activity VALUES(?, ?, ?, ?, ?, ?)''',
		(3334444, "Cut grass", 44, 8675309, 1,"Jan-29-2018"))

#=================================================
print("==> Crew")
c.execute('''CREATE TABLE IF NOT EXISTS crew
			(	name TEXT,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO crew VALUES(?, ?, ?)''',
		("Cleaning", 1,"Jan-11-2018"))


#=================================================
print("==> Crew_member")
c.execute('''CREATE TABLE IF NOT EXISTS crew_member
			(	crew_id INTEGER,
				employee_id INTEGER,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO crew_member VALUES(?, ?, ?, ?)''',
		(4445555, 3456789, 2, "Mar-7-2017"))


#================================================
print("==> Customer")
c.execute('''CREATE TABLE IF NOT EXISTS customer
			(	name TEXT,
				email TEXT,
				street TEXT,
				city TEXT,
				state TEXT,
				zip TEXT,
				phone TEXT,
				status_id INTEGER,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO customer VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Fred Nelson", "fredTHELadiesMAN@gmail.com", "2232 Rutherford blvd.", "Boro","TN","37167", "615-555-3333", 2, 1,"Jan-10-2018"))

#===============================================
print("==> Employee")
c.execute('''CREATE TABLE IF NOT EXISTS employee
			(	name TEXT,
				email TEXT,
				phone TEXT,
				password TEXT,
				message TEXT,
				status_id INTEGER,
				active INTEGER,
				date_created TEXT)''')
c.execute('''INSERT INTO employee VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',("John Doe", "Doe12@gmail.com", 615-555-8966, "password", "This guy is cool",2345 , 1, "Jan-1-2018"))

#==============================================
print("==> Equipment")
c.execute('''CREATE TABLE IF NOT EXISTS equipment
			(	name TEXT,
				quantity INTEGER,
				crew_id INTEGER,
				active INTEGER)''')

c.execute('''INSERT INTO equipment VALUES(?, ?, ?, ?)''',("Mower", 4, 4545, 1))



#==============================================
print("==> Notification")
c.execute('''CREATE TABLE IF NOT EXISTS notification
			(	type TEXT,
				note TEXT,
				customer_id INTEGER,
				employee_id INTEGER,
				status_id INTEGER,
				active INTEGER,
				date_created TEXT)''')
c.execute('''INSERT INTO notification VALUES(?, ?, ?, ?, ?, ?, ?)''',("unknown", "This guy is cool", 433443, 343534, 23423,2345, "Jan-1-2018"))


#================================================
print("==> Schedule")
c.execute('''CREATE TABLE IF NOT EXISTS schedule
			(	type TEXT,
				customer_id INTEGER,
				employee_id INTEGER,
				active INTEGER,
				schedule_date TEXT,
				date_created TEXT)''')
c.execute('''INSERT INTO schedule VALUES(?, ?, ?, ?, ?, ?)''',("This gus is cool", 23, 2332, 1, "Aug-3-2018", "June-3-2018"))


#================================================
print("==> Session")
c.execute('''CREATE TABLE IF NOT EXISTS session
			(	user_id INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO session VALUES(?, ?)''',(23, "May-23-18"))


#===============================================
print("==> Status")
c.execute('''CREATE TABLE IF NOT EXISTS status
			(	name TEXT,
				description TEXT,
				status_group TEXT,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO status VALUES(?, ?, ?, ?, ?)''',("John Doe", "Cuts grass", "Manager", 2, "Jan-5-2018"))


#=============================================
print("==> Todo")
c.execute('''CREATE TABLE IF NOT EXISTS todo
			(	type TEXT CHECK (type IN ("RFQ", "Complaint")),
				customer_id INTEGER,
				status_id INTEGER,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO todo VALUES(?, ?, ?, ?, ?)''',("RFQ", 4345453, 23, 1, "July-1-2018"))


#=============================================
print("==> User")
c.execute('''CREATE TABLE IF NOT EXISTS user
			(
				email TEXT,
				password TEXT,
				employee_id INTEGER,
				customer_id INTEGER,
				status_id INTEGER,
				active INTEGER,
				date_created TEXT)''')

c.execute('''INSERT INTO user VALUES(?, ?, ?, ?, ?, ?, ?)''',("Doe12@gmail.com","password", 12321, 23232, 444444, 1, "Jan-1-2018"))



conn.commit() # SAVE CHANGES TO DATABASE	
