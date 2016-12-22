FROM kprpi

RUN apt-get install -y phpldapadmin

COPY ./config.php /etc/phpldapadmin/config.php

RUN chgrp www-data /etc/phpldapadmin/config.php

EXPOSE 80

ENTRYPOINT ["/usr/bin/entry.sh"]

CMD apachectl -DFOREGROUND
