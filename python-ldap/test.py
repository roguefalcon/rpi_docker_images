#!/usr/bin/python

import ldap
import ldap.modlist as modlist

l = ldap.initialize("ldap://192.168.1.139")
l.simple_bind_s("cn=admin,dc=pyatt,dc=lan","qwerty")
try:
   #l.search_s("cn=admin,dc=pyatt,dc=lan", ldap.SCOPE_SUBTREE, "objectclass=*")
   print l.search_s('ou=Group,dc=pyatt,dc=lan', ldap.SCOPE_SUBTREE,'(cn=kpyatt*)',['cn','objectClass','Password'])
except:
   print "Didn't find that user"

import ldif

"""
dn = "cn=foobar,ou=Group,dc=pyatt,dc=lan"
insertLDIF = {}
#insertLDIF['ou'] = ['People','Group']
insertLDIF['objectClass'] = ['posixGroup','top']
insertLDIF['gidNumber'] = ['550']
insertLDIF['memberUid'] = ['foobar']
insertLDIF['userpassword'] = ['barfoo']

#myLDIF = ldif.CreateLDIF(dn, insertLDIF)
#print myLDIF

# Send the add LDIF
newldif = modlist.addModlist(insertLDIF)
#l.add_s(dn, newldif)
print "Added to group: Group"
"""

# This adds a new user to Docuwiki
dn = "cn=Foo Bar,ou=People,dc=pyatt,dc=lan"
insertLDIF = {}
insertLDIF['cn'] = ['Foo Bar']
insertLDIF['gidNumber'] = ['500']
insertLDIF['givenName'] = ['Foo']
insertLDIF['homeDirectory'] = ['/home/users/foobar']
insertLDIF['objectClass'] = ['inetOrgPerson','posixAccount','top']
insertLDIF['userpassword'] = ['barfoo']
insertLDIF['sn'] = ['Bar']
insertLDIF['userid'] = ['foobar']
insertLDIF['uidNumber'] = ['1002']
insertLDIF['ou'] = ['People','Group']

myLDIF = ldif.CreateLDIF(dn, insertLDIF)
print myLDIF

# Send the add LDIF
newldif = modlist.addModlist(insertLDIF)
l.add_s(dn, newldif)
print "Added to group: People"

# All done here
l.unbind_s()
