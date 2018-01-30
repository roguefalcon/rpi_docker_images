#!/usr/bin/python3

#imported libraries
import sqlite3

#the sql conn and cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

print("==> activities")
c.execute('''SELECT todo_id, note, status_id, employee_id, active, date_created FROM activity''')
activities = c.fetchall()

for act in activities:
    print(act)

print('==> crew')
c.execute('''SELECT name, active, date_created FROM crew''')
crews = c.fetchall()

for crew in crews:
	print(crew)

print('==> crew member')
c.execute('''SELECT crew_id, employee_id, active, date_created FROM crew_member''')
cmems = c.fetchall()

for cm in cmems:
	print(cm)

print('==> customer')
c.execute('''SELECT name, email, street, city, state, zip, phone, status_id, active, date_created FROM customer''')
custs = c.fetchall()

for cu in custs:
	print(cu)

print("==> employees")
c.execute ('''SELECT name, email, street, city, state, zip, phone, status_id, active, date_created FROM customer''')
employees = c.fetchall()

for emp in employees:
    	print(emp)

print('==> equipment')
c.execute('''SELECT name, quantity, crew_id, active FROM equipment''')
equipment = c.fetchall()

for eq in equipment:
	print(eq)

print('==> notifications')
c.execute('''SELECT type, note, customer_id, employee_id, status_id, active, date_created FROM notification''')
noties = c.fetchall()

for note in noties:
	print(note)

print('==> schedules')
c.execute('''SELECT type, customer_id, employee_id, active, schedule_date, date_created FROM schedule''')
sched = c.fetchall()

for s in sched:
	print(s)

print('==> sessions')
c.execute('''SELECT user_id, date_created FROM session''')
sessions = c.fetchall()

for sesh in sessions:
	print(sesh)

print('==> statuses')
c.execute('''SELECT name, description, status_group, active, date_created FROM status''')
statuses = c.fetchall()

for stat in statuses:
	print(stat)

print('==> todo list')
c.execute('''SELECT type, customer_id, status_id, active, date_created FROM todo''')
todo = c.fetchall()

for td in todo:
	print(td)

print('==> Users')
c.execute('''SELECT email, password, employee_id, customer_id, status_id, active, date_created FROM user''')
users = c.fetchall()

for u in users:
	print(u)




