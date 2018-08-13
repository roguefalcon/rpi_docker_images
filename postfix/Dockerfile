FROM alpine:edge

# Postfix myhostname
ENV HOSTNAME=mail.pyattdevtraining.com
# Host that relays your msgs
ENV RELAYHOST=
# An (optional) username for the relay server
ENV RELAYHOST_USERNAME=
# An (optional) login password for the relay server
ENV RELAYHOST_PASSWORD=
# Allow domains from per Network ( default 127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 )
ENV MYNETWORKS=127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16
# Allow any sender domains
ENV ALLOWED_SENDER_DOMAINS=pyattdevtraining.com

# Install supervisor, postfix and bash (because run.sh is not sh-complatible)
RUN        true && \
           apk add --no-cache --update postfix ca-certificates supervisor rsyslog bash && \
           apk add --no-cache --upgrade musl musl-utils && \
           (rm "/tmp/"* 2>/dev/null || true) && (rm -rf /var/cache/apk/* 2>/dev/null || true)

# Set up configuration
COPY       supervisord.conf /etc/supervisord.conf
COPY       rsyslog.conf /etc/rsyslog.conf
COPY       run.sh /run.sh
COPY       virtual /etc/postfix/virtual
RUN        chmod +x /run.sh

# Set up spool volume
VOLUME     [ "/var/spool/postfix", "/etc/postfix" ]

# Run supervisord
USER       root
WORKDIR    /tmp

EXPOSE     587
ENTRYPOINT ["/run.sh"]
