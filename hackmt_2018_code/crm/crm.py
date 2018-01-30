#!/usr/bin/python3

# Include Flask and setup the application object
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import flash
import bcrypt
import sqlite3
app = Flask(__name__)

# The SQL connection ==========================================================
conn = sqlite3.connect('sql.db', check_same_thread=False)
# This tells SQLite that I want dictionaries instead of tuples for fetch statements
conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
# SQL cursor
c = conn.cursor()

# The index page
@app.route("/")
def index():
    return render_template("login.html")

# Login =======================================================================
@app.route("/login", methods=["POST"])
def login():

   # First let's confirm they sent us a username and password.
   if not request.form['username'] or not request.form['password']:
      flash("No username or password entered")

      return redirect(url_for("index"))

   print(request.form['username'])
   # Let's check their password against the database
   c.execute('SELECT name, password FROM employee WHERE name=?', (request.form['username'],))
   user = c.fetchone()
    
   print(user)
   # Let's check the bcrypt password
   if bcrypt.checkpw(request.form['password'].encode('utf8'), user['password']):
      flash('success')
    
      # This actually 'logs' the user in by saving the username in the session
      session['username'] = request.form['username'] # Take them to the browse page (they made it in)
      return redirect(url_for("browse"))

   # The login didn't work
   else:

      # Let's tell them they need to try again
      flash("Login failed")

   # We need to go back to the index page
   return redirect(url_for("todo_browse"))

# browse ==========================================================================
@app.route("/browse")
def todo_browse():

   # Let's query the database and pull the entries
   c.execute('''SELECT 
                       t.rowid, t.todo_type, c.name, c.street, 
                       c.city, c.state, c.zip, c.phone
		  FROM todo t, customer c
	         WHERE t.customer_id = c.rowid''')
   data = c.fetchall()

   # Send these to the template
   return render_template("browse.html", data=data)

# delete ==========================================================================
@app.route("/delete/<id>")
def todo_delete(id):

   # Delete the todo item from the database
   c.execute('''DELETE FROM todo 
                      WHERE rowid = ?''', (id, ))

   # Save the database to disk
   conn.commit()

   # Send user back to the browse screen
   return redirect(url_for("todo_browse"))

@app.route("/read/<id>")
def todo_read(id):

   # Get a single customer from the list
   c.execute('''SELECT c.name, c.street, c.city, c.state, c.zip, c.phone 
                  FROM customer c
                 WHERE c.rowid = ?''', (id, ))
   data = c.fetchone()

   # send a populated template
   return render_template("read.html", data=data)


# Runtime settings =================================================================
if __name__ == "__main__":
	# sets up Flask Sessions
    app.secret_key = 'Ssa0dfloi30s9adflkj3/{}asdf9#@'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0', port=5000, debug=True)
