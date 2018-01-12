#!/usr/bin/python

from flask import Flask, url_for
from flask import render_template, redirect
from flask import request, send_from_directory
from flask import make_response, flash
from tinydb import TinyDB, Query, where
import ldap
import ldap.modlist as modlist
import sys, os
import random
import sqlite3
from dns import resolver
import subprocess
from pipes import quote
import shlex

# The flask app object
app = Flask(__name__)

# Initialize the database
db = TinyDB('db.json')
conn = sqlite3.connect('sql.db', check_same_thread=False)
# This tells SQLite that I want dictionaries instead of tuples for fetch statements
conn.row_factory = lambda c, r: dict([(col[0], r[idx]) for idx, col in enumerate(c.description)])
c = conn.cursor()

# Registration Info Screen
@app.route("/")
def main():

   data = {}

   # This will find a free VM
   #vms = Query()
   #free_vms = db.search(vms.username == '')
   c.execute('''SELECT * from vms WHERE username = ""''')
   free_vms = c.fetchall()
   if free_vms:

      # Have they already registered
      if request.cookies.get('username'):
         data['username'] = request.cookies.get('username')

      return render_template('user_registration.html', data=data) 
   else:
      return render_template('registration_full.html') 


# Register a new user =========================================================
@app.route("/register", methods=['POST'])
def register():

   print "==> Setting up: " + request.form['username']

   # The form fields
   name = request.form['name']
   email = request.form['email']
   username = request.form['username']
   password = request.form['password']
   filename = username + '.ovpn'

   # Let's see if this username is free
   c.execute('''SELECT username FROM vpn_users WHERE username=?''', (username,))
   user = c.fetchone()

   # We need to tell them if a name is already taken
   if user:
      print "==> flashing message to user"
      flash('Username ' + str(username) + ' already exists.  Sorry :(')
      return redirect(url_for('main'))

   # Add the user
   c.execute('''INSERT INTO vpn_users VALUES (?, ?, ?, ?, ?)''', 
            (name, email, username, password, filename))
   rowid = c.lastrowid

   # Assign VM ================================================================
   vm_name = selectRandomVM(username)

   # Create the LDAP User via the request object
   setupLDAPUser()

   # Create the VPN settings
   setupVPN(rowid)

   # Now let's close the db
   conn.commit()

   # We want to set a cookie for this user so we can track who it is
   resp = make_response(redirect(url_for('vpn_setup')))
   resp.set_cookie('username', username, max_age=2592000)
   resp.set_cookie('vm_name', vm_name, max_age=2592000)

   return resp


@app.route("/vpn_setup")
def vpn_setup():

   return render_template('vpn_setup.html')


@app.route("/vpn_setup_windows")
def vpn_setup_windows():

   return render_template('vpn_setup_windows.html')


@app.route("/hello_world")
@app.route("/hello_world/<page_id>")
def hello_world(page_id=None):

   if page_id:
       return render_template('hello_world' + str(page_id) + '.html')
   else:
       return render_template('hello_world.html')


@app.route("/rest_api")
def rest_api():

   return render_template('rest_api.html')


@app.route("/dashboard")
def dashboard():

   # Get a list of the users registered
   c.execute('''SELECT name, email, username, filename FROM vpn_users''')
   users = c.fetchall()

   # Get a list of the vms 
   c.execute('''SELECT name, ip, username from vms''')
   vms = c.fetchall()

   # Show the results
   return render_template('dashboard.html', vms=vms, users=users) 


# Success Screen
@app.route("/vm/new", methods=['POST'])
def new_vm():

   # Setup OSTicket User (note: This is the only place MySQL is used so I hardcoded somethings)
   import MySQLdb
   mydb=MySQLdb.connect(user='kproot',passwd="qwer",db="osticket",host='127.0.0.1')
   myc=mydb.cursor()
   myc.execute("""INSERT INTO ost_staff(dept_id, role_id, username, firstname, lastname, passwd, isactive, isadmin, isvisible,
                                      max_page_size, permissions, created, updated, signature)
                              VALUES (4,2,%s,%s,%s,MD5(%s),1,0,1,25,'{"faq.manage":1}', now(), now(), '') """,
                       (request.form['username'], request.form['firstname'], request.form['lastname'], request.form['password'])
            )
   myc.execute("""SELECT staff_id FROM ost_staff WHERE username = %s""", (request.form['username']))
   myrow = myc.fetchone()
   myc.execute("""insert into ost_team_member (team_id, staff_id, flags) VALUES (1,%s,1)""", (myrow[0]));
   mydb.commit()

   # Local Database ===========================================================
   # Update the local tinydb database
   db.update({'username': request.form['username'], 'password': request.form['password'], 'firstname': request.form['firstname'], 'lastname': request.form['lastname'], 'language': request.form['language']}, vms.name == vm_name)

   return render_template('vm_assignment.html', vm_name=vm_name) 


# Favicon.ico ==================================================================
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

# OpenVPN file download ========================================================
@app.route('/ovpn_file', methods=['GET', 'POST'])
def ovpn_file():

   # Set the username from the cookie of the user that is logged in 
   # I don't want to be obvious and expose other ovpn files
   filename = request.cookies.get('username') + '.ovpn'

   # the full path to the ovpn files
   fileloc = os.path.join(app.root_path, 'static/ovpns/')

   # Send the file as an attachment
   return send_from_directory(directory=fileloc, filename=filename, as_attachment=True)


# HELPER FUNCTIONS =============================================================

# Let's select and assign a random VM
def selectRandomVM(username):

   # Get a list of the unassigned VMs
   c.execute('''SELECT name, ip FROM vms WHERE username = ""''')
   free_vms = c.fetchall()
   random_vm = random.choice(free_vms)
   vm_name = random_vm['name']
   print "==> Selecting vm: " + str(vm_name)
   c.execute('''UPDATE vms SET username = ? WHERE name = ?''', (username, vm_name))
   # There is a chance here that two people could get the same random VM before the database update
   # is commited.  It's a small chance but there is a chance.

   # Let's determine the IP address of this vm by DNS lookup
   res = resolver.Resolver()
   res.nameservers = ['192.168.1.112']
   answers = res.query(vm_name)
   ip = answers[0].address
   print "==> Found IP: " + ip

   # Determine the ODROID ip address so we know which host to start the VM on.
   odroid = ip[:-1] + "0"

   # Let's create the requested VM on the odroid host via ansible
   # NOTE I needed to give them more ports so I went with 5000 to 5050.  Seems like 50 will be enough
   os.system("ansible " + odroid + " -m command -a \"docker run --name " + vm_name + " -d --restart always -p " + ip + ":22:22 -p " + ip + ":80:80 -p " + ip + ":5000-5050:5000-5050 -h " + vm_name + " python_dev\"")

   return vm_name


# Setup the LDAP user
def setupLDAPUser():

   # User Setup ===============================================================
   # Let's get the last user id number from a file
   with open('last_uid.txt') as f:
      last_uid = f.read()

   # Connect to LDAP and add new user
   l = ldap.initialize("ldap://192.168.1.112")
   l.simple_bind_s("cn=admin,dc=pyatt,dc=lan","asdf")

   # This adds a new user to Docuwiki and SSH
   dn = "cn=" + str(request.form['name']) + ",ou=People,dc=pyatt,dc=lan"
   insertLDIF = {}
   insertLDIF['cn'] = [str(request.form['name'])]
   insertLDIF['gidNumber'] = ['500']
   insertLDIF['givenName'] = [str(request.form['name'])]
   insertLDIF['homeDirectory'] = ['/home/' + str(request.form['username'])]
   insertLDIF['objectClass'] = ['inetOrgPerson','posixAccount','top']
   insertLDIF['userpassword'] = [str(request.form['password'])]
   insertLDIF['sn'] = ['lastname']
   insertLDIF['userid'] = [str(request.form['username'])]
   insertLDIF['uidNumber'] = [str(int(last_uid) + 1)]
   insertLDIF['ou'] = ['People','Group']
   insertLDIF['loginShell'] = ['/bin/bash']

   # This prints an LDIF file
   import ldif
   myLDIF = ldif.CreateLDIF(dn, insertLDIF)
   print myLDIF

   # Send the add LDIF
   newldif = modlist.addModlist(insertLDIF)
   l.add_s(dn, newldif)

   # Increment the UID now that LDAP has a new user
   with open('last_uid.txt', 'w') as f:
      f.write(str(int(last_uid) + 1))

   return


# Setup VPN
def setupVPN(rowid):

   username = request.form['username']
   password = request.form['password']
   ipaddress = '10.8.0.' + str(rowid + 5)
   print "==> Using VPN ip: " + ipaddress

   # This runs the pivpn command to add a new user
   command = "/usr/local/bin/pivpn add --name {}".format(quote(username))
   command += " --password {}".format(quote(password))
   subprocess.call(shlex.split(command), shell=False)

   # create the client config file to assign routes and ip addresses
   with open('/etc/openvpn/clients/' + username, 'w') as f:
      f.write('ifconfig-push ' + ipaddress + ' 255.255.255.0\n')
      f.write('push "route 192.168.1.0 255.255.255.0 10.8.0.1"\n')
      f.write('push "route 192.168.3.0 255.255.255.0 10.8.0.2"\n')

   command = "cp /home/pi/ovpns/{}.ovpn ./static/ovpns/.".format(quote(username))
   subprocess.call(shlex.split(command), shell=False)

   return


# Application Settings =========================================================
if __name__ == "__main__":
    app.secret_key = '8sad87das87sdf87sdf87sd87fd87dsf'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0', port=3500, debug=True)
