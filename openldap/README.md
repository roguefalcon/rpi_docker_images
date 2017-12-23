# OpenLDAP

This image runs a version of OpenLDAP (slapd).

To build it:

```docker build -t openldap openldap/```

To start it:

```docker run --name openldap -d --restart always -p 389:389 openldap```

Then you will need to setup the intial database.  I'm sure there is a way to do this in configs but I had to do the following:

```ldapadd -x -D 'cn=admin,dc=pyatt,dc=lan' -w asdf -f base.ldif```

This setup is very insecure so we will need to do the ldap password has trick before the Hack-a-thon.
