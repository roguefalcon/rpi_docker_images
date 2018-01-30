#!/usr/bin/python3
from mobileapi import app
from flask import jsonify
from flask import request
from flask import g
import datetime

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named user_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""


# Get a list of users (Browse) ==========================================
@app.route('/api/1.0/user', methods=['GET'])
def user_browse():

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
    g.c.execute('''SELECT rowid, email, active, date_created, customer_id, employee_id, status_id
                     FROM user
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)

# Insert Single user (Add) ===============================================
@app.route('/api/1.0/user', methods=['POST'])
def user_add():

    # User input
    email = request.form.get('email')
    password = request.form.get('password')
    customerId = request.form.get('customerId')

    # Let's tell the user they forget to send values we need
    if not email:
        return jsonify({'success': False, 'error': 'Missing email address.'})
    if not password:
        return jsonify({'success': False, 'error': 'Missing password.'})
    if not customerId:
        return jsonify({'success': False, 'error': 'Missing customerId.'})

    g.c.execute('''
                  INSERT INTO user
                       VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (email, password,0,customerId,1,1,datetime.datetime.now()))

    # Let's get the id of the item we just inserted so
    # We can tell the user which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})

# Get Data for a single user (Read) ======================================
@app.route('/api/1.0/user/<user_id>', methods=['GET'])
def user_read(user_id):

    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT rowid, email, active, date_created, customer_id, employee_id, status_id
                    FROM user
                   WHERE active = 1
                     AND rowid = ?
                ''', (user_id))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)


# Delete Single user (Delete) ============================================
@app.route('/api/1.0/user/<user_id>', methods=['DELETE'])
def user_delete(user_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE user
                      SET active=0
                    WHERE rowid=?''', user_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})

@app.route("/api/1.0/user/login", methods=["POST"])
def user_login():

    email = request.form.get('email')
    password = request.form.get('password')

    # First let's confirm they sent us a username and password.
    if not email:
        return jsonify({'success': False, 'error': 'Missing email address.'})
    if not password:
        return jsonify({'success': False, 'error': 'Missing password.'})

   # Let's check their password against the database
    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT email, password
                    FROM user
                   WHERE email = ?
                ''', (email,))
    data = g.c.fetchone()
    
    if data == None:
        return jsonify({'success': False})
    
    dbEmail = data['email']
    dbPassword = data['password']
    if dbEmail == email and dbPassword == password:
        g.c.execute('''
                  SELECT rowid, customer_id, customer_id, email
                    FROM user
                   WHERE email = ?
                ''', (email,))
        userInfo = g.c.fetchone()
        #Let's tell them it worked
        return jsonify({'success': True, 'result': userInfo})

    # The login didn't work
    else:

        return jsonify({'success': False})