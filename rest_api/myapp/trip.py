#!/usr/bin/python3
# Trip API - v1.0

from myapp import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named trip_[bread_keyword].  This will avoid naming collisions.
"""


# Get a list of trips (Browse) ==========================================
@app.route('/api/1.0/trip', methods=['GET'])
def trip_browse():

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
    g.c.execute('''
                   SELECT t.rowid,
                          c.make,
                          c.model,
                          p.name,
                          d.street,
                          d.city,
                          d.state,
                          d.zip_code,
                          trip_start_time,
                          trip_end_time
                     FROM trip t, car c, passenger p, destination d
                    WHERE t.car_id = c.rowid
                      AND t.passenger_id = p.rowid
                      AND t.destination_id = d.rowid
                    LIMIT ?''', (limit,))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)


# Get Data for a single trip (Read) ======================================
@app.route('/api/1.0/trip/<trip_id>', methods=['GET'])
def trip_read(trip_id):

    # Return the all columns for this one employee
    g.c.execute('''
                   SELECT t.rowid,
                          c.make,
                          c.model,
                          p.name,
                          d.street,
                          d.city,
                          d.state,
                          d.zip_code,
                          trip_start_time,
                          trip_end_time
                     FROM trip t, car c, passenger p, destination d
                    WHERE t.car_id = c.rowid
                      AND t.passenger_id = p.rowid
                      AND t.destination_id = d.rowid
                      AND t.rowid = ?
                ''', (trip_id,))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)


# Update Single Trip (Edit) ==============================================
@app.route('/api/1.0/trip/<trip_id>', methods=['PUT'])
def trip_edit(trip_id):

    # User input
    car_id = request.form.get('car_id')
    passenger_id = request.form.get('passenger_id')
    destination_id = request.form.get('destination_id')
    trip_start_time = request.form.get('trip_start_time')
    trip_end_time = request.form.get('trip_end_time')

    # Let's tell the user they forget to send values we need
    if (not car_id or not passenger_id or not destination_id or
        not trip_start_time or not trip_end_time):
       return jsonify({'success': False, 'error': 'Missing values'})

    # Update the trip in the database
    g.c.execute('''
                  UPDATE trip
                     SET car_id=?,
                         passenger_id=?,
                         destination_id=?,
                         trip_start_time=?,
                         trip_end_time=?
                   WHERE rowid=?
                ''', (car_id, passenger_id, destination_id, trip_start_time, trip_end_time, trip_id))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Insert Single Trip (Add) ===============================================
@app.route('/api/1.0/trip', methods=['POST'])
def trip_add():

    # User input
    car_id = request.form.get('car_id')
    passenger_id = request.form.get('passenger_id')
    destination_id = request.form.get('destination_id')
    trip_start_time = request.form.get('trip_start_time')
    trip_end_time = request.form.get('trip_end_time')

    # Let's tell the user they forget to send values we need
    if (not car_id or not passenger_id or not destination_id or
        not trip_start_time or not trip_end_time):
       return jsonify({'success': False, 'error': 'Missing values'})

    # Insert the new trip into the database
    g.c.execute('''
                  INSERT INTO trip
                       VALUES (?, ?, ?, ?, ?)
                ''', (car_id, passenger_id, destination_id, trip_start_time, trip_end_time))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Delete Single Trip (Delete) ============================================
@app.route('/api/1.0/trip/<trip_id>', methods=['DELETE'])
def trip_delete(trip_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''DELETE FROM trip
                    WHERE rowid=?''', trip_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
