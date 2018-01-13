#!/usr/bin/python3
# Passenger API - v1.0

from myapp import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named passenger_[bread_keyword].  This will avoid naming collisions.
"""


# Get a list of passengers (Browse) ==========================================
@app.route('/api/1.0/passenger', methods=['GET'])
def passenger_browse():

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
    g.c.execute('''SELECT rowid, name, active
                     FROM passenger
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)


# Get Data for a single passenger (Read) ======================================
@app.route('/api/1.0/passenger/<passenger_id>', methods=['GET'])
def passenger_read(passenger_id):

    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT rowid, name, active
                    FROM passenger
                   WHERE active = 1
                     AND rowid = ?
                ''', (passenger_id))
    data = g.c.fetchall()

    # Return in JSON format
    return jsonify(data)


# Update Single Passenger (Edit) ==============================================
@app.route('/api/1.0/passenger/<passenger_id>', methods=['PUT'])
def passenger_edit(passenger_id):

    # User input
    name = request.form.get('name')

    # Let's tell the user they forget to send values we need
    if not name:
       return jsonify({'success': False, 'error': 'Missing values'})

    g.c.execute('''
                  UPDATE passenger
                     SET name=?,
                         active=1
                   WHERE rowid=?
                ''', (name, passenger_id))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Insert Single Passenger (Add) ===============================================
@app.route('/api/1.0/passenger', methods=['POST'])
def passenger_add():

    # User input
    name = request.form.get('name')

    # Let's tell the user they forget to send values we need
    if not name:
       return jsonify({'success': False, 'error': 'Missing values'})

    g.c.execute('''
                  INSERT INTO passenger
                       VALUES (?, ?)
                ''', (name, 1))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Delete Single Passenger (Delete) ============================================
@app.route('/api/1.0/passenger/<passenger_id>', methods=['DELETE'])
def passenger_delete(passenger_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE passenger
                      SET active=0
                    WHERE rowid=?''', passenger_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
