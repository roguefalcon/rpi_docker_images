#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import os
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/register", methods = ["POST"])
def register():
    APP_URL = 'crmapi.pyatt.lan'
    APP_PORT = '80'

    if 'APP_PORT' in os.environ:
        APP_PORT = int(os.environ['APP_PORT'])

    if 'APP_URL' in os.environ and os.environ['APP_DEBUG'] == '0':
        APP_APP = str(os.environ['APP_URL'])
    
    data = {'name' : request.form.get('name'), 'email': request.form.get('email'), 'phone': request.form.get('phone'), 'street': request.form.get('street'), 'city': request.form.get('city'), 'state': request.form.get('state'), 'zipcode': request.form.get('zip')} 

    r = requests.post('http://' + APP_URL + '/api/1.0/customer', data=data)

    return redirect(url_for('thank_you'))

@app.route("/thank_you")
def thank_you():
    return render_template("thankyou.html")


if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

