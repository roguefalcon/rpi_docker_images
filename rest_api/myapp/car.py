#!/usr/bin/python3
# Car API - v1.0

from myapp import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named car_[bread_keyword].  This will avoid naming collisions.
"""


# Get a list of cars (Browse) ==========================================
@app.route('/api/1.0/car', methods=['GET'])
def car_browse():

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
    g.c.execute('''SELECT rowid, make, model, year, mileage, active
                     FROM car
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)


# Get Data for a single car (Read) ======================================
@app.route('/api/1.0/car/<car_id>', methods=['GET'])
def car_read(car_id):

    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT rowid, make, model, year, mileage, active
                    FROM car
                   WHERE active = 1
                     AND rowid = ?
                ''', (car_id))
    data = g.c.fetchall()

    # Return in JSON format
    return jsonify(data)


# Update Single Car (Edit) ==============================================
@app.route('/api/1.0/car/<car_id>', methods=['PUT'])
def car_edit(car_id):

    # User input
    make = request.form.get('make')
    model = request.form.get('model')
    year = request.form.get('year')
    mileage = request.form.get('mileage')

    # Let's tell the user they forget to send values we need
    if not make or not model or not year or not mileage:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Update the car in the database
    g.c.execute('''
                  UPDATE car
                     SET make=?,
                         model=?,
                         year=?,
                         mileage=?
                   WHERE rowid=?
                ''', (make, model, year, mileage, car_id))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Insert Single Car (Add) ===============================================
@app.route('/api/1.0/car', methods=['POST'])
def car_add():

    # User input
    make = request.form.get('make')
    model = request.form.get('model')
    year = request.form.get('year')
    mileage = request.form.get('mileage')

    # Let's tell the user they forget to send values we need
    if not make or not model or not year or not mileage:
       return jsonify({'success': False, 'error': 'Missing values'})

    # Insert the new car into the database
    g.c.execute('''
                  INSERT INTO car
                       VALUES (?, ?, ?, ?, ?)
                ''', (make, model, year, mileage, 1))
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True})


# Delete Single Car (Delete) ============================================
@app.route('/api/1.0/car/<car_id>', methods=['DELETE'])
def car_delete(car_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE car
                      SET active=0
                    WHERE rowid=?''', car_id)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})
