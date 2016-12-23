#!/bin/bash

mysqld &
sleep 10
mysql -e "CREATE USER 'kproot'@'%' IDENTIFIED BY 'qwer';GRANT ALL PRIVILEGES ON *.* TO 'kproot'@'%' WITH GRANT OPTION;FLUSH PRIVILEGES;"
sleep 5
killall mysqld
