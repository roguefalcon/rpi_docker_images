#!/usr/bin/python3
from mobileapi import app
from flask import jsonify
from flask import request
from flask import g
from flask import Flask

#BREAD
#Browse
@app.route('/api/1.0/notification', methods=['GET'])
def notification_browser():

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
    g.c.execute(''' SELECT *
                   FROM notification
                   WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    return jsonify(data)

#Read
@app.route('/api/1.0/notification/<id>', methods=['GET'])
def notification_read(id):


    g.c.execute(''' SELECT *
                   FROM notification
                   WHERE rowid = ?
                ''', (id))
    data = g.c.fetchone()

    return jsonify(data)


#Edit
@app.route('/api/1.0/notification/<id>', methods=['PUT'])
def notification_edit(id):
    return "Notification endpoint edit id " + id

#Add
@app.route('/api/1.0/notification', methods=['POST'])
def notification_add():
    # User input
    type = request.form.get('type')
    note = request.form.get('note')
    customer_id = request.form.get('customer_id')
    employee_id = request.form.get('employee_id')
    status_id = request.form.get('status_id')
    active = request.form.get('active')
    date_created = request.form.get('date_created')

    g.c.execute('''
                  INSERT INTO notification
                       VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (type, note, customer_id, employee_id, status_id, active, date_created))

    # Let's get the id of the item we just inserted so
    # We can tell the user which record they created
    rowid = g.c.lastrowid

    # Save the changes to the database
    g.conn.commit()

    # Let's tell them it worked
    return jsonify({'success': True, 'rowid': rowid})

@app.route('/api/1.0/notification/<id>', methods=['DELETE'])
def notification_delete():
    return "Notification delete "

# Runtime settings
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
