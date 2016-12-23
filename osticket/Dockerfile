FROM kprpi

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install nginx unzip

COPY nginx.conf /nginx.conf

RUN mkdir /osticket

COPY osTicket-v1.10.zip /osticket/osticket.zip

WORKDIR /osticket

RUN unzip osticket.zip

EXPOSE 80

CMD nginx -c /nginx.conf -g "pid /var/run/nginx.pid;"
