# Python Imports
from flask import Flask
from flask import g
from flask import session
from flask import request
from flask import redirect
import sqlite3

# Setup my flask object
app = Flask(__name__)

# Database Connection =========================================================
@app.before_request
def db_connect():

    try:
        # The SQL connection ==================================================
        g.conn = sqlite3.connect('sql.db', check_same_thread=False)
        # This tells SQLite that I want dictionaries
        # instead of tuples for fetch statements
        g.conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(g.c.description)])
        # SQL cursor
        g.c = g.conn.cursor()
    except RuntimeError:
        print("FATAL: No database connection established")


@app.route('/')
def index():

    return "The Operations API in our Autonomous Lawn Mower website is used for administrative purposes. The user would be able to view the different Lawn Mower crews in each city we operate in, edit or delete data regarding crew members and scheduling, as well as updating employee statuses as active or inactive."


# App Modules =================================================================
from opsapi import employee
from opsapi import crew
from opsapi import equipment
from opsapi import schedule
