from alpine:latest

# Setup alpine with php, nginx and supporting libraries
RUN apk update && apk add bzip2 nginx php7 php7-fpm php7-opcache php7-gd php7-mysqli php7-zlib php7-curl php7-ctype php7-bz2 php7-curl php7-dom php7-iconv php7-json php7-mcrypt php7-mysqli php7-mysqlnd php7-openssl php7-pdo_mysql php7-sockets php7-xml php7-zip php7-imagick php7-ftp zendframework php7-tokenizer

# Setup phpBB3
COPY phpBB-3.2.2.tar.bz2 /tmp/phpBB-3.2.2.tar.bz2
RUN bunzip2 /tmp/phpBB-3.2.2.tar.bz2 && \
    tar xvf /tmp/phpBB-3.2.2.tar && \
    rm /tmp/phpBB-3.2.2.tar && \
    mkdir /run/nginx && \
    mv phpBB3/* /var/www/localhost/htdocs/.

# Load the config and startup files
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh

# Set permissions
RUN chmod 666 /var/www/localhost/htdocs/config.php && \
    chmod 777 /var/www/localhost/htdocs/files && \
    chmod 777 /var/www/localhost/htdocs/cache && \
    chmod 777 /var/www/localhost/htdocs/store && \
    chmod 777 /var/www/localhost/htdocs/images/avatars/upload

ENTRYPOINT ["/entrypoint.sh"]

CMD ["php-fpm7", "-F"]
#CMD ["sleep", "10000"]
