#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Index Page
@app.route("/")
def index():
    return render_template("index.html")

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)
