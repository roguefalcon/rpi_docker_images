#!/usr/bin/python3
# Customer API - v1.0

from crmapi import app
from flask import jsonify
from flask import request
from flask import g

#BREAD: Browse, Read, Edit, Add, Delete

@app.route('/api/1.0/customer', methods=['GET'])
def customer_browse():

    active = request.args.get('active', default='1', type = int)

    limit = request.args.get('limit', default='100', type = int)

    # Get customer records=============================
    g.c.execute('''SELECT rowid, name, email, street, city, state, zip, phone,
                          status_id, active, date_created
                   FROM customer
                   WHERE active=?
                   LIMIT ?''', (active, limit))
    data = g.c. fetchall()

    #Data back to JSON
    return jsonify(data)

#Get Data for a single customer (READ)==========================
@app.route('/api/1.0/customer/<customer_id>', methods=['PUT'])
def customer_edit(customer_id):

    #User input
    name = request.form.get('name')
    email = request.form.get('email')
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')
    phone = request.form.get('phone number')
    date_created = request.form.get('date')

    #Prompt protecc
    if not name or not email or not street or not city or not state
    or not zipcode or not  phone or not date:
        return jsonify({'success':False,'error': 'Missing values'})
   
    #Update Customer into database
    g.c.execute('''
                 UPDATE customer
                    SET name=?,
                        email=?,
                        street=?,
                        city=?,
                        state=?,
                        zipcode=?,
                        phone=?,
                        date=?
                  WHERE rowid=?
                ''', (name,email,street,city,state,zipcode,phone,date))
    g.conn.commit()
    #Tell user it worked
    return jsonify({'success':True, 'rowid':customer_id
