FROM kprpi

RUN apt-get install slapd ldap-utils

RUN dpkg-reconfigure slapd

EXPOSE 389 636

ENTRYPOINT ["/usr/bin/entry.sh"]

CMD slapd -d 32768 -u openldap -g openldap
