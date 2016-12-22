# Uncomment the lines below to cleanup everything and build from scratch
#docker rm kprpi openldap phpldapadmin dokuwiki
#docker rmi kprpi openldap phpldapadmin dokuwiki

# Start with my base image from resin/rpi-raspbian:jessie-20160830
cd kprpi
docker build -t kprpi .
cd ..

# Now we need to build openldap
cd openldap
docker build -t openldap .
cd ..

# Let's build phpLDAPadmin so we can admin it
cd phpldapadmin
docker build -t phpldapadmin .
cd ..

# Dokuwiki
cd dokuwiki
docker build -t dokuwiki .
cd ..

# Jenkins
cd jenkins
docker build -t jenkins .
cd ..

# Start the containers
#docker run --name openldap -d -p 389:389 -p 636:636 openldap
docker run --name phpldapadmin -d -p 8080:80 phpldapadmin
docker run --name dokuwiki -d -p 80:80 dokuwiki
docker run --name jenkins -d -p 8000:8000 jenkins
