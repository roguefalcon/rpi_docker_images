#!/usr/bin/python3
# Equipment API - v1.0

from opsapi import app
from flask import jsonify
from flask import request
from flask import g

# Get a list of equipment (browse)
@app.route('/api/1.0/equipment', methods=['GET'])
def equipment_browse():
    
    
    active = request.args.get('active', default='1', type=int)

    limit = request.args.get('limit', default='10', type=int)

    g.c.execute('''SELECT rowid, name, quantity, crew_id, active
		FROM equipment WHERE active=? LIMIT ?''', (active, limit))
    data = g.c.fetchall()

    return jsonify(data)

@app.route('/api/1.0/equipment/<equipment_id>', methods=['GET'])
def equipment_read(equipment_id):

    g.c.execute('''SELECT rowid, name, quantity, crew_id, active FROM equipment
		where active = 1 AND rowid = ?''',(equipment_id))
    data = g.c.fetchone()

    return jsonify(data)
@app.route('/api/1.0/equipment/<equipment_id>', methods=['PUT'])
def equipment_edit(equipment_id):

    # Get user data
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    crew_id = request.form.get('crew_id')

    if not name or not quantity or not crew_id:
       return jsonify({'Success':False, 'Error':'Missing values'})

    g.c.execute('''UPDATE equipment SET name=?,quantity=?,crew_id=?,
		active=1 WHERE rowid=?''', (name, quantity, crew_id,equipment_id))

    g.conn.commit()

    return jsonify({'Success':True, 'rowid':equipment_id})

@app.route('/api/1.0/equipment', methods=['POST'])
def equipment_add():

    
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    crew_id = request.form.get('crew_id')

    if not name or not quantity or not crew_id:
       return jsonify({'Success':False, 'Error':'Missing values'})
    g.c.execute('''INSERT INTO equipment VALUES (?,?,?,?)''', (name, quantity,
		crew_id,1))

    rowid = g.c.lastrowid

    g.conn.commit()

    return jsonify({'Success':True, 'rowid': rowid})

