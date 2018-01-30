#!/usr/bin/python3
# Car API - v1.0

from crmapi import app 
from flask import jsonify
from flask import request
from flask import g


# Imported libraries
import sqlite3
import os

@app.route('/api/1.0/todo', methods=['GET'])
def todo_browse():

    # Indicates whether something has been deleted
    active = request.args.get('active', default='1', type=int)

    # Protects the server
    limit = request.args.get('limit', default='10', type=int)
    # Table
    g.c.execute('''SELECT rowid,todo_type, customer_id, status_id, active, date_created
                     FROM todo
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Sending JSON
    return jsonify(data)


# Read
@app.route('/api/1.0/todo/<todo_id>', methods=['GET'])
def todo_read(todo_id):

    # Return the columns 
    g.c.execute('''
                  SELECT rowid, todo_type, customer_id, status_id, active, date_created
                    FROM todo
                   WHERE active = 1
                     AND rowid = ?
                ''', (todo_id))
    data = g.c.fetchall()

    # Returns in JSON
    return jsonify(data)


# Edit
@app.route('/api/1.0/todo/<todo_id>', methods=['PUT'])
def todo_edit(todo_id):

    # User input
    todo_type = request.form.get('todo_type')
    customer_id = request.form.get('customer_id')
    status_id = request.form.get('status_id')
    active = request.form.get('active')
    date_created = request.form.get('date_created')

    # Let's tell the user they forget to send values we need
    if not todo_type or not customer_id or not status_id or not active or not date_created:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Update the todo table in the database
    g.c.execute('''
                  UPDATE todo
                     SET customer_id=?,
                         status_id=?,
                         active=?,
			 date_created=?,
			 todo_type=?
                   WHERE rowid=?
                ''', (customer_id, status_id, active, date_created, todo_type,todo_id))

    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': todo_id})


# Insert Single todo (Add) ===============================================
@app.route('/api/1.0/todo', methods=['POST'])
def todo_add():

    # User input
    customer_id = request.form.get('customer_id')
    status_id = request.form.get('status_id')
    active = request.form.get('active')
    date_created = request.form.get('date_created')
    todo_type = request.form.get('todo_type')
    # Let's tell the user they forget to send values we need
    if not customer_id or not status_id or not active or not date_created or not todo_type:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Insert the new car into the database
    g.c.execute('''
                  INSERT INTO todo
                       VALUES (?, ?, ?, ?, ?,?)
                ''', (customer_id, status_id, active, date_created, todo_type,1))

    # Let's get the id of the item we just inserted so
    # We can tell the user which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})


# Delete Single Car (Delete) ============================================
@app.route('/api/1.0/todo/<todo_id>', methods=['DELETE'])
def todo_delete(todo_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE todo
                      SET active=0
                    WHERE rowid=?''', todo_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
