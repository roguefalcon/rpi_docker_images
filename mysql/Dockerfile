FROM kprpi

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install mysql-server

COPY my.cnf /etc/mysql/my.cnf

COPY grant_access.sh /tmp/grant_access.sh
RUN chmod 755 /tmp/grant_access.sh
RUN /bin/bash /tmp/grant_access.sh

EXPOSE 3306

CMD mysqld
