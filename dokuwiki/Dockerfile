FROM kprpi

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install lighttpd php5-cgi php5 dokuwiki php-net-ldap

RUN ln /etc/dokuwiki/lighttpd.conf /etc/lighttpd/conf-available/50-dokuwiki.conf

COPY ./local.php /etc/dokuwiki/local.php
COPY ./10-fastcgi.conf /etc/lighttpd/conf-enabled/10-fastcgi.conf

RUN lighttpd-enable-mod dokuwiki

EXPOSE 80

CMD lighttpd -D -f /etc/lighttpd/lighttpd.conf
