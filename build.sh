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
#docker run --name openldap -d -p 389:389 -p 636:636 openldap
#docker run --name phpldapadmin -d -p 8080:80 phpldapadmin
#docker run --name dokuwiki -d -p 80:80 dokuwiki
#docker run --name jenkins -d -p 8000:8000 jenkins
