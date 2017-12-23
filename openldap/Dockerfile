# This is modified from the version by Daniel Guerra

FROM alpine

ENV OPENLDAP_VERSION 2.4.44-r0

RUN  apk update \
  && apk add openldap openldap-back-mdb \
  && rm -rf /var/cache/apk/*

VOLUME ["/etc/openldap-dist", "/var/lib/openldap"]

COPY modules/ /etc/openldap/modules

COPY entrypoint.sh /entrypoint.sh
RUN chmod u+x entrypoint.sh
RUN mkdir /run/openldap
RUN touch /run/openldap/slapd.pid
RUN chmod a+rw /run/openldap/slapd.pid
RUN touch /run/openldap/slapd.args
RUN chmod a+rw /run/openldap/slapd.args
COPY slapd.conf /etc/openldap/slapd.conf
COPY slapd.ldif /etc/openldap/slapd.ldif

EXPOSE 389

ENTRYPOINT ["/entrypoint.sh"]

CMD ["slapd", "-d", "32768", "-u", "ldap", "-g", "ldap"]
