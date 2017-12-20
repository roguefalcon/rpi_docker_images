#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
import bcrypt
import sqlite3

app = Flask(__name__)


# The SQL connection ==========================================================
conn = sqlite3.connect('sql.db', check_same_thread=False)
# This tells SQLite that I want dictionaries instead of tuples for fetch statements
conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
# SQL cursor
c = conn.cursor()



# Index Page ==================================================================
@app.route("/")
def index():

   # Are they logged in?
   if session and 'username' in session:
      print("Found: " + session['username'])
      return redirect(url_for("browse"))

   # The front page template
   return render_template("index.html")


# Login =======================================================================
@app.route("/login", methods=["POST"])
def login():

   # This actually 'logs' the user in by saving the username in the session
   session['username'] = request.form['username']

   # Take them to the browse page
   return redirect(url_for("browse"))


# Logout =====================================================================
@app.route("/logout")
def logout():

   # Log them out
   session.pop('username', None)

   # Send them to the index page
   return redirect(url_for("index"))


# Create ======================================================================
@app.route("/create")
def html_form():

   return render_template("create.html")


# Save ========================================================================
@app.route("/save", methods=["POST"])
def save():

   # We want to save this response to the database
   c.execute('INSERT INTO favorite_color VALUES(?, ?)', (request.form['name'], request.form['color']))

   # Commit causes the system to write to the database file
   conn.commit()

   return redirect(url_for('browse'))


# Browse ======================================================================
@app.route("/browse")
def browse():

   # Let's query the database and pull the entries
   c.execute('SELECT rowid, name, color FROM favorite_color')
   data = c.fetchall()

   # Send these to the template
   return render_template("browse.html", data=data)


# Edit =========================================================================
@app.route("/edit/<id>")
def edit(id):

   data = {}   
   c.execute('SELECT rowid, name, color FROM favorite_color WHERE rowid=?', (id,))
   data = c.fetchone()

   return render_template("edit.html", data=data)


# Update =======================================================================
@app.route("/update", methods=["POST"])
def update():

   # We want to save this response to the database
   c.execute('UPDATE favorite_color SET name = ?, color=? WHERE rowid = ?', (request.form['name'], request.form['color'], request.form['id']))

   # Commit causes the system to write to the database file
   conn.commit()

   return redirect(url_for('browse'))


# Delete =======================================================================
@app.route("/delete/<id>")
def delete(id):

   # Delete without confirming anything
   c.execute('DELETE FROM favorite_color WHERE rowid=?', (id,))

   # Commit causes the system to write to the database file
   conn.commit()
   
   # We want to take the user back to the browse screen
   return redirect(url_for('browse'))


# Run the application
if __name__ == "__main__":
    # Setting up Flask Sessions
    app.secret_key = 'Ssa0dfloi30s9adflkj3/{}asdf9#@'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0', port=5500, debug=True)
