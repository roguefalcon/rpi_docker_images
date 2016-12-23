# The base image for the raspberry pi
FROM kprpi

# Updates
RUN apt-get -y update && apt-get -y upgrade

# Install everything
RUN apt-get -y install nginx unzip php5-common php5-cli php5-fpm php5-mysql php5-gd php5-intl php5-apcu

# Setup Nginx
COPY nginx.conf /nginx.conf

# Setup OSTicket
RUN mkdir /osticket
COPY osTicket-v1.10.zip /osticket/osticket.zip
WORKDIR /osticket
RUN unzip osticket.zip
RUN chmod a+x /osticket/upload/*.php
COPY ost-config.php /osticket/upload/include/ost-config.php
RUN chmod 0644 /osticket/upload/include/ost-config.php

# Setup PHP5-FPM
COPY www.conf /etc/php5/fpm/pool.d/www.conf

# This is where the world is going to see it
EXPOSE 80

# Starts php5-fpm and nginx
COPY start.sh /start.sh
RUN chmod u+x /start.sh
CMD /start.sh
