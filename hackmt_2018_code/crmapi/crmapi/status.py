#!/usr/bin/python3
# Status API - v1.0

from crmapi import app
from flask import jsonify
from flask import request
from flask import g

"""
   I prefer the BREAD acryonm: Browse, Read, Edit, Add and Delete
   So to protect the scope of the entire application functions will
   be named status_[bread_keyword].  This will avoid naming collisions
   across our entire python module.
"""

# Get a list of statuses (Browse) ==========================================
@app.route('/api/1.0/status', methods=['GET'])
def status_browse():
    # The active flag shows only the 'non-deleted' items
    # If you want to see everything pass active=0
    active = request.args.get('active', default='1', type=int)

    # It is a best practice to limit the amount of data an
    # API will allow a user to retrieve on a single call
    # This creates a throttle to protect the server.
    # In this case we are just defaulting to 10 but will let
    # them ask for more
    limit = request.args.get('limit', default='10', type=int)
    
    # Get status records
    g.c.execute('''SELECT rowid, 
			  name, 
	                  description, 
			  status_group, 
	                  active, 
	                  date_created
		     FROM status
		    WHERE active=?
		    LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    # Send the data back as JSON
    return jsonify(data)

# Get Data for a single status (Read) ========================================
@app.route('/api/1.0/status/<status_id>', methods=['GET'])
def status_read(status_id):

    # Return all the columns for the application
    g.c.execute('''
	           SELECT rowid,
	                  name,
	                  description,
	                  status_group,
	                  active,
	                  date_created
	             FROM status
	            WHERE active = 1
	              AND rowid = ?
	            	  ''', (status_id))
    data = g.c.fetchone()

    # Return in JSON format
    return jsonify(data)	
