#!/usr/bin/python3
# Customer API - v1.0

from crmapi import app
from flask import jsonify
from flask import request
from flask import g
import datetime

#BREAD: Browse, Read, Edit, Add, Delete

@app.route('/api/1.0/customer', methods=['GET'])
def customer_browse():

    #active flag shows only the 'non'deleted' items
    #If you want to see everything set pass active = 0
    active = request.args.get('active', default='1', type = int)
    
    #Best practice to limit API to one call
    #Set for up to 100
    limit = request.args.get('limit', default='100', type = int)

    # Get customer records(BROWSE)============================
    g.c.execute('''SELECT rowid, name, email, street, city, state, zip, phone,
                          status_id, active, date_created
                   FROM customer
                   WHERE active=?
                   LIMIT ?''', (active, limit))
    data = g.c. fetchall()

    #Data back to JSON
    return jsonify(data)

#Get Data for a single Customer (READ)=============================
@app.route('/api/1.0/customer/<customer_id>', methods=['GET'])
def customer_read(customer_id):

     #Return the all columns for this one customer
     g.c.execute('''
                   SELECT rowid, name, email, street, city, state, zip, phone, status_id, active, date_created
                     FROM customer
                    WHERE active = 1
                      AND rowid = ?
                 ''', (customer_id))
     data = g.c.fetchall()
     
     # Return in JSON format
     return jsonify (data)

#Get Data for a single customer (EDIT)==========================
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
    status_id = request.form.get('status id')

    #Prompt protecc
    if not name or not email or not street or not city or not state or not zipcode or not phone or not status_id:
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
                        statusid=?,
                  WHERE rowid=?
                ''', (name,email,street,city,state,zipcode,phone,status_id,))
    g.conn.commit()
    #Tell user it worked
    return jsonify({'success':True, 'rowid':customer_id})

# Insert Single Customer (ADD)=========================================
@app.route('/api/1.0/customer', methods=['POST'])
def customer_add():

    # USer Input
    name = request.form.get('name')
    email = request.form.get('email')
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')
    phone = request.form.get('phone')
    status_id = 1
    date_created = datetime.datetime.now()

    #Tell the user they forgot to send values if necessary
    if not name or not email or not street or not city or not state or not zipcode or not phone:
        return jsonify({'success':False, 'error':'Missing values'})

    #Insert new customer into database
    g.c.execute('''
                  INSERT INTO customer
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                ''',(name, email, street, city, state, zipcode, phone, status_id, 1, date_created))

    #get id of the customer
    rowid = g.c.lastrowid

    #Save chamges
    g.conn.commit()
    
    #Confirm it worked
    return jsonify({'success': True, 'rowid': rowid})

#Delete a Single Customer (DELETE)=================================
@app.route('/api1.0/customer/<customer_id>', methods=['DELETE'])
def customer_delete(customer_id):
    
    #Set active flag to 0 which will make them appear deleted
    g.c.execute(''' UPDATE customer
                       SET active=0
                     WHERE rowid=?''', customer_id)
    g.conn.commit()
    
    #Tell the user it worked
    return jsonify({'success':True})
