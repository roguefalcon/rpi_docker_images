# Uncomment the lines below to cleanup everything and build from scratch
#docker rm kprpi openldap phpldapadmin dokuwiki
#docker rmi kprpi openldap phpldapadmin dokuwiki

# Start with my base image from resin/rpi-raspbian:jessie-20160830
docker build -t kprpi kprpi/

# Now we need to build openldap
docker build -t openldap openldap/

# Let's build phpLDAPadmin so we can admin it
docker build -t phpldapadmin pypldapadmin/

# Dokuwiki
docker build -t dokuwiki dokuwiki/

# Jenkins
docker build -t jenkins jenkins/

# ostikcet
docker build -t osticket osticket/

# ostikcet
docker build -t mysql mysql/

# Start the containers
#docker run --name mysql -d --restart always -p 3306:3306 mysql
#docker run --name openldap -d -p 389:389 -p 636:636 openldap
#docker run --name phpldapadmin -d --restart always -p 8080:80 phpldapadmin
#docker run --name dokuwiki -d --restart always -p 192.168.2.10:80:80 dokuwiki
#docker run --name jenkins -d --restart always -p 8000:8000 jenkins
#docker run --name osticket -d --restart always -p 192.168.2.11:80:80 osticket
#docker run --name skyblue.pyatt.lan -d --restart always -p 192.168.1.53:22:22 -p 192.168.1.53:80:80 -p 192.168.1.53:5000:5000 -h skyblue.pyatt.lan ubuntu_dotnet_dev
