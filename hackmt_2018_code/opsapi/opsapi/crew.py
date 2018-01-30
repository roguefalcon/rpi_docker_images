#!/usr/bin/python3
# Crew API - v1.0

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


# Get a list of the crews (Browse) ==========================================
@app.route('/api/1.0/crew', methods=['GET'])
def crew_browse():

    # The active flag shows only the 'non-deleted' items
    # If you want to see everything pass active=0
    active = request.args.get('active', default='1', type=int)

    # It is a best practice to limit the amount of data an
    # API will allow a user to retrieve on a single call
    # This creates a throttle to protect the server.
    # In this case we are just defaulting to 10 but will let
    # them ask for more
    limit = request.args.get('limit', default='10', type=int)

    # Get the crew records
    # NOTE: not querying password on purpose
    g.c.execute('''SELECT rowid, name, active, date_created
                     FROM crew
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)


# Get Data for a single crew (Read) ======================================
@app.route('/api/1.0/crew/<rowid>', methods=['GET'])
def crew_read(rowid):

    # Return the all columns for this one crew
    g.c.execute('''
                  SELECT rowid, name, active, date_created
                    FROM crew
                   WHERE active = 1
                     AND rowid = ?
                ''', (rowid))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)


# Update Single Crew (Edit) ==============================================
@app.route('/api/1.0/crew/<rowid>', methods=['PUT'])
def crew_edit(rowid):

    # User input
    name = request.form.get('name')

    # Let's tell the user they forget to send values we need
    if not name:
       return jsonify({'success': False, 'error': 'Missing values'})

    g.c.execute('''
                  UPDATE crew
                     SET name=?,
                         active=1
                   WHERE rowid=?
                ''', (name, rowid))

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})


# Insert Single Crew (Add) ===============================================
@app.route('/api/1.0/crew', methods=['POST'])
def crew_add():

    # User input
    name = request.form.get('name')

    # Let's tell the user they forget to send values we need
    if not name:
       return jsonify({'success': False, 'error': 'Missing values'})

    g.c.execute('''
                  INSERT INTO crew
                       VALUES (?, ?)
                ''', (name, 1))

    # Let's get the id of the item we just inserted so
    # We can tell the user which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})


# Delete Single Crew (Delete) ============================================
@app.route('/api/1.0/crew/<rowid>', methods=['DELETE'])
def crew_delete(rowid):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE crew
                      SET active=0
                    WHERE rowid=?''', rowid)
    g.conn.commit()

    # Tell the user it worked
    return jsonify({'success': True})


