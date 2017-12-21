from kprpi

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y php php-pear php-mdb2 apache2 vim aptitude curl wget

ENV LDAP_PORT 389
ENV FUSIONDIRECTORY_VERSION 1.0.19-1
ENV FUSIONDIRECTORY_DEB_PKG_VERSION 1.0.19-1
ENV LDAP_HOST 192.168.1.112
ENV LDAP_SERVER_URL ldap://${LDAP_HOST}:${LDAP_PORT}
ENV LDAP_ROOT Manager

RUN apt-get update && \
    apt-get install -y argonaut-server fusiondirectory=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-mail=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-systems=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-ldapdump=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-ldapmanager=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-weblink=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-plugin-webservice=${FUSIONDIRECTORY_DEB_PKG_VERSION} \
    fusiondirectory-webservice-shell=${FUSIONDIRECTORY_DEB_PKG_VERSION}


ADD image/root/ /

RUN chown -R root:root /usr/share/fusiondirectory/include/jsonrpcphp/ && \
    a2dissite 000-default && \
    a2disconf fusiondirectory && \
    a2ensite fusiondirectory

EXPOSE 80

ENV LDAP_DOMAIN='pyatt.lan'
ENV LDAP_ROOTPW='asdf'
RUN chmod a+x /start-fd

CMD ["/start-fd"]
