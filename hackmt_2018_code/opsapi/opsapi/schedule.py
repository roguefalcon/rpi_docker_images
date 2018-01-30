#!/usr/bin/python3
#schedule API
from opsapi import app
from flask import jsonify
from flask import request
from flask import g
import datetime

@app.route('/api/1.0/schedule', methods=['GET'])
def schedule_browse():
	
	#The active flag shows only the 'non-deleted' items
	# If you want to see everything pass active=0
	active = request.args.get('active', default='1',type=int)

	#limit the user to a certain amount of data that 
	#can be retrieved at a single time.
	limit = request.args.get('limit', default='10', type=int)

	# Get the employee records
	g.c.execute('''SELECT rowid, type, customer_id, employee_id, active,
					schedule_date, date_created FROM schedule
					WHERE active=? LIMIT ?''', (active, limit))

	data = g.c.fetchall()

	return jsonify(data)

@app.route('/api/1.0/schedule/<rowid>', methods=['GET'])
def schedule_read(rowid):

	g.c.execute('''SELECT rowid, type, customer_id, employee_id, active,
					schedule_date, date_created FROM schedule
					WHERE active = 1 AND rowid = ?''', (rowid))
	data = g.c.fetchone() #because only fetches one row

	return jsonify(data)

####NOT EDITING THE SCHEDULE!!!
@app.route('/api/1.0/schedule/<rowid>', methods=['PUT'])
def schedule_edit(rowid):
	temp_date = datetime.datetime.now()
	Type = request.form.get("type")
	customer_id = request.form.get("customer_id")
	employee_id = request.form.get("employee_id")
	schedule_date = request.form.get("schedule_date")
	date_created = temp_date.strftime('%m-%d-%y')
	

	if not Type or not customer_id or not employee_id or not schedule_date:
		return jsonify({'success': False, 'error': 'Missing values'})

	g.c.execute('''
					UPDATE schedule 
									SET type=?,
										customer_id=?,
										employee_id=?,
										active =?,
										schedule_date=?,
										date_created=?
									WHERE rowid=?
								''',(Type, customer_id, employee_id, 1, schedule_date, date_created, rowid))
	
	g.conn.commit()
	return jsonify({'success': True, 'rowid': rowid})


@app.route('/api/1.0/schedule', methods=['POST'])
def schedule_add():
	temp_date = datetime.datetime.now()
	Type = request.form.get("type")
	customer_id = request.form.get("customer_id")
	employee_id = request.form.get("employee_id")
	schedule_date = request.form.get("schedule_date")
	date_created = temp_date.strftime('%m-%d-%y')
	

	if not Type or not customer_id or not employee_id or not schedule_date:
		print(Type, customer_id, employee_id, schedule_date, date_created)
		return jsonify({'success': False, 'error': 'Missing values'})

	g.c.execute('''INSERT INTO schedule VALUES (?,?,?,?,?,?)''',
					(Type, customer_id, employee_id, 1, schedule_date, date_created))

	rowid = g.c.lastrowid
	
	g.conn.commit()
	return jsonify({'success': True, 'rowid': rowid})

@app.route('/api/1.0/schedule/<rowid>', methods=['DELETE'])
def schedule_delete(rowid):
	g.c.execute('''UPDATE schedule
					SET active=0
					WHERE rowid=?''', rowid)
	g.conn.commit()

	return jsonify({'success':True})
