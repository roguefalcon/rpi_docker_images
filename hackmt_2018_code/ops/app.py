#!/usr/bin/python3

#include Flask and setup the application object
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import re
import bcrypt
import requests
import sqlite3
import datetime as dt

app = Flask(__name__)
# The sql conn
conn = sqlite3.connect('sql.db', check_same_thread=False)
conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
# sql cursor
c = conn.cursor()
#the index page
@app.route("/")
def index():
	return render_template("index.html")
	r = request.get("load_sql.py")
	data=[r.json()]
    #r = requests.get('http://copper.pyatt.lan:5000/api/1.0/schedule')
    #x = requests.get('http://copper.pyatt.lan:5013/api/1.0/customer')
    
    #r = requests.get('http://opsapi.pyatt.lan/api/1.0/schedule')
    #custid = r.json().cust_id
    #url = 'http://crmapi.pyatt.lan/api/1.0/customer/' + string(custid)
    #x = requests.get(url)
    #print(r.json())
    #return render_template("schedule.html", data=[r.json(),x])

# Load the schedule.html page with some data
@app.route("/schedule")
def schedule():
    r = requests.get('http://crmapi.pyatt.lan/api/1.0/customer')
    return render_template("schedule.html",data=r.json())
#Equipment page
@app.route("/equipment")
def equipment():
    r = requests.get('http://opsapi.pyatt.lan/api/1.0/equipment')
    print(r.json())
    return render_template("equipment.html", data=r.json())

#Login
@app.route("/login", methods=["POST"])
def login():
	d = dt.datetime.now()
	date = d.strftime('%m/%d/%y')
	if not request.form['username'] or not request.form['password']:
		flash("No username or password entered")
		return redirect(url_for("index"))
	else:
	    return redirect(url_for("schedule"))

@app.route("/browse")
def browse():
    c.execute('SELECT rowid, name, color FROM favorite_color')
    data = c.fetchall()
    return render_template("browse.html", data=data)
@app.route("/logout")
def logout(): 
	return redirect(url_for("index"))


# Runtime settings
if __name__ == "__main__":
    app.secret_key = 'Ssa0dfloi30s9adflkj3/{}asdf9#@'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=5000, debug=True)
