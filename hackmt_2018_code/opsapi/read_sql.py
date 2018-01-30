#!/usr/bin/python3
import sqlite3

# The sql connection & cursor

conn = sqlite3.connect('sql.db')
c = conn.cursor()

# List Cars

#========================================================================================
print("==> Activity")
c.execute('''SELECT todo_id,
                    note,
                    statue_id,
                    employee_id,
                    active,
                    date_created
                FROM activity''')
data = c.fetchall()

for item in data:
    print(item)

#List Activites

#=======================================================================================

print("==> Crew")
c.execute('''SELECT name,
                    active,
                    date_created
                FROM crew''')
data = c.fetchall()

for item in data:
    print(item)

# List Crew

#========================================================================================
print("==> Crew_member")
c.execute('''SELECT crew_id,
                    employee_id,
                    active,
                    date_created
                FROM crew_member''')
data = c.fetchall()

for item in data:
    print(item)

#List Crew Members

#=======================================================================================

print("==> Customer")
c.execute('''SELECT name,
                    email,
                    street,
                    city,
                    state,
                    zip,
				    phone,
		    		status_id,
		    		active,
					date_created
                FROM customer''')
data = c.fetchall()

for item in data:
    print(item)

print("==> Employee")
c.execute('''SELECT name,
					email,
					phone,
					password,
					message,
					status_id,
					active,
					date_created
				FROM employee''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Equipment")
c.execute('''SELECT name,
					quantity,
					crew_id,
					active
				FROM equipment''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Notification")
c.execute('''SELECT type,
					note,
					customer_id,
					employee_id,
					status_id,
					active,
					date_created
				FROM notification''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Schedule")
c.execute('''SELECT type,
					customer_id,
					employee_id,
					active,
					schedule_date,
					date_created
				FROM schedule''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Session")
c.execute('''SELECT user_id,
					date_created
				FROM session''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Status")
c.execute('''SELECT name,
					description,
					status_group,
					active,
					date_created
				FROM status''')

data = c.fetchall()

for item in data:
	print(item)

print("==> Todo")
c.execute('''SELECT type,
					customer_id,
					status_id,
					active,
					date_created
				FROM todo''')

data = c.fetchall()

for item in data:
	print(item)

print("==> User")
c.execute('''SELECT email,
					password,
					employee_id,
					customer_id,
					status_id,
					active,
					date_created
				FROM user''')

data = c.fetchall()

for item in data:
	print(item)


