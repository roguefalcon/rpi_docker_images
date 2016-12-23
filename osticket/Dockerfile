FROM kprpi

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install nginx unzip

COPY nginx.conf /nginx.conf

COPY osTicket-v1.10.zip /tmp/osticket.zip

RUN mkdir /osticket

RUN unzip /tmp/osticket.zip /osticket

EXPOSE 80

CMD /usr/bin/nginx -t -c ~/mynginx.conf -g "pid /var/run/nginx.pid; worker_processes 1;"
