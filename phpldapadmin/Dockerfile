FROM debian:latest

RUN apt-get update && apt-get upgrade -y

RUN apt-get -f install -y ucf php php-ldap apache2 php-xml openvpn

COPY phpldapadmin.ovpn /phpldapadmin.ovpn
COPY entry.sh /usr/bin/entry.sh
COPY ./config.php /etc/phpldapadmin/config.php
RUN chgrp www-data /etc/phpldapadmin/config.php

COPY ./phpldapadmin_1.2.2-6.1_all.deb /phpldapadmin_1.2.2-6.1_all.deb
RUN dpkg -i /phpldapadmin_1.2.2-6.1_all.deb

EXPOSE 80

ENTRYPOINT ["/usr/bin/entry.sh"]

CMD apachectl -DFOREGROUND
