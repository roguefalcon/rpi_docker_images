#!/usr/bin/python3
# Employee API - v1.0

from crmapi import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named passenger_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""


# Get a list of passengers (Browse) ==========================================
@app.route('/api/1.0/employee', methods=['GET'])
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
    # NOTE: not querying password on purpose
    g.c.execute('''SELECT rowid, name, email, active
                     FROM employee
                    WHERE active=?
                    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)
