FROM kprpi

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y php7-ldap php7-cli libapache2-mod-php7 phpldapadmin

COPY ./config.php /etc/phpldapadmin/config.php

RUN chgrp www-data /etc/phpldapadmin/config.php

EXPOSE 80

ENTRYPOINT ["/usr/bin/entry.sh"]

CMD apachectl -DFOREGROUND
