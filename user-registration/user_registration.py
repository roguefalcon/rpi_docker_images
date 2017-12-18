#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import request, send_from_directory
from tinydb import TinyDB, Query, where
import ldap
import ldap.modlist as modlist
import sys, os
import random
import sqlite3
app = Flask(__name__)

# Initialize the database
db = TinyDB('db.json')

# Registration Info Screen
@app.route("/")
def main():
   # This will find a free VM
   vms = Query()
   free_vms = db.search(vms.username == '')
   if free_vms:
      return render_template('user_registration.html') 
   else:
      return render_template('registration_full.html') 


@app.route("/vpn_setup")
def vpn_setup():

   return render_template('vpn_setup.html')


@app.route("/vpn_setup_windows")
def vpn_setup_windows():

   return render_template('vpn_setup_windows.html')


@app.route("/hello_world")
def hello_world():

   return render_template('hello_world.html')


@app.route("/vm/list")
def list_vm():
   vms = db.all()
   return render_template('vm_list.html', vms=vms) 


# Success Screen
@app.route("/vm/new", methods=['POST'])
def new_vm():

   # VM Assignment ============================================================
   # This will find a free VM
   vms = Query()
   free_vms = db.search(vms.username == '')
   random_vm = random.choice(free_vms)
   vm_name = random_vm['name']

   print "==> Assigning host", vm_name, "to user", request.form['firstname'], request.form['lastname'], "as", request.form['username'], "with password", request.form['password']

   # Let's create the requested VM on the odroid host via ansible
   os.system("nslookup " + vm_name + " | grep Address | grep -v '#53' | awk '{print $2}' > /tmp/kpout")
   with open('/tmp/kpout') as f:
      lines = f.readlines()
   ip = lines[0].rstrip()
   odroid = ip[:-1] + "0"
   os.system("ansible " + odroid + " -m command -a \"docker run --name " + vm_name + " -d --restart always -p " + ip + ":22:22 -p " + ip + ":80:80 -p " + ip + ":5000:5000 -h " + vm_name + " " + request.form['language'] + "\"")

   # User Setup ===============================================================
   # Let's get the last user id number from a file
   with open('last_uid.txt') as f:
      last_uid = f.read()

   # Connect to LDAP and add new user
   l = ldap.initialize("ldap://192.168.1.5")
   l.simple_bind_s("cn=admin,dc=pyatt,dc=lan","qwerty")

   # This adds a new user to Docuwiki and SSH
   dn = "cn=" + str(request.form['firstname'] + " " + request.form['lastname']) + ",ou=People,dc=pyatt,dc=lan"
   insertLDIF = {}
   insertLDIF['cn'] = [str(request.form['firstname'] + " " + request.form['lastname'])]
   insertLDIF['gidNumber'] = ['500']
   insertLDIF['givenName'] = [str(request.form['firstname'])]
   insertLDIF['homeDirectory'] = ['/home/' + str(request.form['username'])]
   insertLDIF['objectClass'] = ['inetOrgPerson','posixAccount','top']
   insertLDIF['userpassword'] = [str(request.form['password'])]
   insertLDIF['sn'] = [str(request.form['lastname'])]
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

# Favicon.ico =================================================================
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)
