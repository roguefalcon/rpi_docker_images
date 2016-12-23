#!/bin/bash

service php5-fpm start
sleep 5
nginx -c /nginx.conf -g "pid /var/run/nginx.pid;"
