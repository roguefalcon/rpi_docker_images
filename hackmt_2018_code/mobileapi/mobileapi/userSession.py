#!/usr/bin/python3
from mobileapi import app
from flask import jsonify
from flask import request
from flask import g
import datetime

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named session_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""


# Get a list of sessions (Browse) ==========================================
@app.route('/api/1.0/session', methods=['GET'])
def session_browse():

    # It is a best practice to limit the amount of data an
    # API will allow a session to retrieve on a single call
    # This creates a throttle to protect the server.
    # In this case we are just defaulting to 10 but will let
    # them ask for more
    limit = request.args.get('limit', default='10', type=int)

    # Get the employee records
    # NOTE: not querying password on purpose
    g.c.execute('''SELECT rowid, user_id, date_created
                    FROM session
                    LIMIT ?''', (limit, )
                    )
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)

# Insert Single session (Add) ===============================================
@app.route('/api/1.0/session', methods=['POST'])
def session_add():

    # session input
    userId = request.form.get('userId')

    # Let's tell the session they forget to send values we need
    if not userId:
        return jsonify({'success': False, 'error': 'Missing userId address.'})

    g.c.execute('''
                  INSERT INTO session
                       VALUES (?, ?)
                ''', (userId, datetime.datetime.now()))

    # Let's get the id of the item we just inserted so
    # We can tell the session which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})

# Get Data for a single session (Read) ======================================
@app.route('/api/1.0/session/<session_id>', methods=['GET'])
def session_read(session_id):

    # Return the all columns for this one employee
    g.c.execute('''
                  SELECT rowid, user_id, date_created
                    FROM session
                   WHERE rowid = ?
                ''', (session_id))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)


# Delete Single session (Delete) ============================================
@app.route('/api/1.0/session/<session_id>', methods=['DELETE'])
def session_delete(session_id):

    # Set the active flag to 0 which will make them appear deleted
    g.c.execute('''UPDATE session
                      SET active=0
                    WHERE rowid=?''', session_id)
    g.conn.commit()

    # Tell the session it worked
    return jsonify({'success': True})