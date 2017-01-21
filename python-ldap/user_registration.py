#!/usr/bin/python

from flask import Flask
from flask import render_template
from flask import request
from tinydb import TinyDB, Query, where
import ldap
import ldap.modlist as modlist
app = Flask(__name__)

# Initialize the database
db = TinyDB('db.json')


# Registration Info Screen
@app.route("/")
def main():
    return render_template('user_registration.html') 

@app.route("/vm/list")
def list_vm():
    vms = db.all()
    return render_template('vm_list.html', vms=vms) 


# Success Screen
@app.route("/vm/new", methods=['POST'])
def new_vm():

   # This will find a free VM
   vms = Query()
   free_vms = db.search(vms.username == '')
   vm_name = free_vms[0]['name']

   print "==> Assigning host", vm_name, "to user", request.form['firstname'], request.form['lastname'], "as", request.form['username'], "with password", request.form['password']

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

   import ldif
   # This prints an LDIF file
   myLDIF = ldif.CreateLDIF(dn, insertLDIF)
   print myLDIF

   # Send the add LDIF
   newldif = modlist.addModlist(insertLDIF)
   l.add_s(dn, newldif)

   # Update the local database
   db.update({'username': request.form['username'], 'password': request.form['password'], 'firstname': request.form['firstname'], 'lastname': request.form['lastname']}, vms.name == vm_name)

   # Increment the UID
   with open('last_uid.txt', 'w') as f:
      f.write(str(int(last_uid) + 1))
   
   return render_template('vm_assignment.html', vm_name=vm_name) 

if __name__ == "__main__":
    app.run(host='0.0.0.0')
