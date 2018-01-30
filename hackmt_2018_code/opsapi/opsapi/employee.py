#!/usr/bin/python3
# Employee API - v1.0

from opsapi import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named passenger_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""


# Get a list of passengers (Browse) ==========================================
@app.route('/api/1.0/employee', methods=['GET'])
def employee_browse():

    # The active flag shows only the 'non-deleted' items
    # If you want to see everything pass active=0
    active = request.args.get('active', default='1', type=int)

    # It is a best practice to limit the amount of data an
    # API will allow a user to retrieve on a single call
    # This creates a throttle to protect the server.
    # In this case we are just defaulting to 10 but will let
    # them ask for more
    limit = request.args.get('limit', default='10', type=int)

    # Get the employee records
    # NOTE: not querying password on purpose
    g.c.execute('''SELECT rowid, name, email, active,
		phone, message, status_id, date_created
                     FROM employee
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)
# Get the records of an employee
@app.route('/api/1.0/employee/<employee_id>', methods=['GET'])
def employee_read(employee_id):
    
    # Return all information about an employee
    # DO NOT return the password.
    g.c.execute('''SELECT rowid, name, email, active,
		phone, message, status_id, date_created
		FROM employee
		WHERE active = 1 AND rowid = ?''',
		(passenger_id))
    # Grabbing the one employee
    data = g.c.fetchone()
    # Return in JSON format
    return jsonify(data)
# Updates the records for an employee based on id
@app.route('/api/1.0/employee/<employee_id>', methods=['PUT'])
def employee_edit(employee_id):
    
    # Get input from the user with the updated information
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    status_id = request.form.get('status_id')

    # Tells user if they forget information
    if not name or not email or not phone or not message or not status_id:
       return jsonify({'Success': False, 'error': 'Missing Values'})

    g.c.execute('''UPDATE employee SET name=?, email=?,
		phone=?, message=?, status_id=?, active=1
		WHERE rowid=?''',
		(name, email, phone, message, status_id, employee_id))
    # Update the changes made to the database
    g.conn.commit()

    # Let the user know the changes were successful
    return jsonify({'Success': True, 'rowid':employee_id})

# Adds an employee
@app.route('/api/1.0/employee', methods=['POST'])
def employee_add():
    
    # get user input    
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    message = request.form.get('message')
    status_id = request.form.get('status_id')
    date_created = request.form.get('date_created')

    # Tell the user if they forget a value
    if not name or not email or not phone or not password or not message or not status_id or not date_created:
       return jsonify({'Success': False, 'error': 'Missing Values'})
    
    g.c.execute('''INSERT INTO employee VALUES (?,?,?,?,?,?,?,?)''',
		(name, email, phone, password, message, status_id, 1,
		date_created))
    
    #we get the id of the last item inserted
    rowid = g.c.lastrowid

    #Save changes to the database
    g.conn.commit()

    #Tell the user it was added
    return jsonify({'Success': True, 'rowid':rowid})

# Deletes an employee from the database
@app.route('/api/1.0/employee/<employee_id>', methods=['DELETE'])
def employee_delete(employee_id):

    #set the active flag to 0 to appear deleted
    g.c.execute('''UPDATE employee SET active=0 WHERE rowid=?''',employee_id)

    #Push changes to database
    g.conn.commit()
