#!/usr/bin/python3
# Activity API - v1.0

from crmapi import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named activity_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""
 # Get a list of activities (Browse) ==========================================
@app.route('/api/1.0/activity', methods=['GET'])
def activity_browse():
	# The active flag shows only the 'non-deleted' items
	# If you want to see everything pass active=0
	active = request.args.get('active', default='1', type=int)
	# It is a best practice to limit the amount of data an
    	# API will allow a user to retrieve on a single call
    	# This creates a throttle to protect the server.
    	# In this case we are just defaulting to 10 but will let
    	# them ask for more
	limit = request.args.get('limit', default='10', type=int)

	#Get the activity records
	g.c.execute('''SELECT rowid,
	                      todo_id,
	                      note,
	                      status_id,
	                      employee_id,
	                      active,
	                      date_created
	                 FROM activity
	                WHERE active=?
	                LIMIT ?''', (active, limit))
	data = g.c.fetchall()

	# Send the data back as JSON
	return jsonify(data)

# Get Data for a single activity (Read) ======================================
@app.route('/api/1.0/activity/<activity_id>', methods=['GET'])
def activity_read(activity_id):

    # Return all the columns for activity
    g.c.execute('''
                  SELECT rowid,
                         todo_id,
                         note,
                         status_id,
                         employee_id,
                         active,
                         date_created
                    FROM activity
                   WHERE active=?
                     AND rowid = ?
                ''', (activity_id))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)

# Update Single Activity (Edit)===============================================
@app.route('/api/1.0/activity/<activity_id>', methods=['PUT'])
def activity_edit(activity_id):

    #User input
    todo_id = request.form.get('todo id')
    note = request.form.get('note')
    status_id = request.form.get('status_id')
    employee_id = request.form.get('employee_id')
    
    #Let's tell the user they forget to send values we need
    if not todo_id or not note or not status_id or not employee_id:
       return jsonify({'success': False, 'error': 'Missing values'})
    
    #Update the activity in the database
    g.c.execute('''
                  UPDATE activity
                     SET todo id=?,
                         note=?,
                         status_id=?,
                         employee id=?
                   WHERE rowid=?
                ''', (todo_id, note, status, employee_id))
    g.conn.commit() 

     #Update user of success
    return jsonify({'success': True, 'rowid':activity_id})

# Insert Single Activity (Add) ===============================================
@app.route('/api/1.0/activity', methods=['POST'])
def activity_add():

    # User input
    date_created = request.form.get('date_created')
    employee_id = request.form.get('employee_id')
    note = request.form.get('note')
    status_id = request.form.get('status_id')
    todo_id = request.form.get('todo_id')    

    # Let's tell the user they forget to send values we need
    if not date_created:
       return jsonify({'success': False, 'error': 'Missing values'})
    if not note:
       return jsonify({'success': False, 'error': 'Missing values'})
    if not status_id:
       return jsonify({'success': False, 'error': 'Missing values'})
    if not status_id:
       return jsonify({'success': False, 'error': 'Missing values'})
    if not todo_id:
       return jsonify({'success': False, 'error': 'Missing values'})

    g.c.execute('''
                  INSERT INTO activity
                       VALUES (?, ?, ?, ?, ?, ?)
                ''', (todo_id, note, status_id, employee_id, 1, date_created))

    # Let's get the id of the item we just inserted so
    # We can tell the user which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})

# Delete Activities (Delete) ============================================
@app.route('/api/1.0/activity/<activity_id>', methods=['DELETE'])
def activity_delete(activity_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE activity
                      SET active=0
                    WHERE rowid=?''', activity_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
