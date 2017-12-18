# docker run -ti -p 53:53/tcp -p 53:53/udp -p 10000:10000 -v /data:/data --name=bind9 bind9
FROM kprpi
RUN apt-get -y update && apt-get -y upgrade

# Bind and the ability to check it out
RUN apt-get -y install bind9 dnsutils apt-transport-https

# webmin repo
RUN echo "deb http://download.webmin.com/download/repository sarge contrib" >> /etc/apt/sources.list

# This is required for webmin.  I had to disable gz compression on indexes
COPY docker-gzip-indexes /etc/apt/apt.conf.d/docker-gzip-indexes
RUN apt-get -y update
RUN apt-get -y install apt-show-versions

# Webmin 
RUN apt-get -y install webmin

# This came from someone else and it works well
# https://github.com/sameersbn/docker-bind
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

ENV BIND_USER=bind \
    BIND_VERSION=1:9.9.5 \
    WEBMIN_VERSION=1.830 \
    DATA_DIR=/data

EXPOSE 53/udp 53/tcp 10000/tcp
VOLUME ["/data"]
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/usr/sbin/named"]
