# PHPLDAPAdmin

This image runs the PHP LDAP Admin tool and connects to the OpenLDAP container in this repo (run that one first).

To build it:

```docker build -t phpldapadmin phpldapadmin/```

To start it:

```docker run --name phpldapadmin -d --restart always -p 8080:80 phpldapadmin```

It should work.  Password is `asdf` which needs to be improved before the Hack-a-thon.
