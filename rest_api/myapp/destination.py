#!/usr/bin/python3
# Destination API - v1.0

from myapp import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named destination_[bread_keyword].  This will avoid naming collisions.
"""


# Get a list of destinations (Browse) ==========================================
@app.route('/api/1.0/destination', methods=['GET'])
def destination_browse():

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
    g.c.execute('''SELECT rowid, street, city, state, zip_code, active
                     FROM destination
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)


# Get Data for a single destination (Read) ======================================
@app.route('/api/1.0/destination/<destination_id>', methods=['GET'])
def destination_read(destination_id):

    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT rowid, street, city, state, zip_code, active
                    FROM destination
                   WHERE active = 1
                     AND rowid = ?
                ''', (destination_id))
    data = g.c.fetchall()

    # Return in JSON format
    return jsonify(data)


# Update Single Destination (Edit) ==============================================
@app.route('/api/1.0/destination/<destination_id>', methods=['PUT'])
def destination_edit(destination_id):

    # User input
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')

    # Let's tell the user they forget to send values we need
    if not street or not city or not state or not zip_code:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Update the destination in the database
    g.c.execute('''
                  UPDATE destination
                     SET street=?,
                         city=?,
                         state=?,
                         zip_code=?
                   WHERE rowid=?
                ''', (street, city, state, zip_code, destination_id))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Insert Single Destination (Add) ===============================================
@app.route('/api/1.0/destination', methods=['POST'])
def destination_add():

    # User input
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')

    # Let's tell the user they forget to send values we need
    if not street or not city or not state or not zip_code:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Insert the new destination into the database
    g.c.execute('''
                  INSERT INTO destination
                       VALUES (?, ?, ?, ?, ?)
                ''', (street, city, state, zip_code, 1))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Delete Single Destination (Delete) ============================================
@app.route('/api/1.0/destination/<destination_id>', methods=['DELETE'])
def destination_delete(destination_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE destination
                      SET active=0
                    WHERE rowid=?''', destination_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
