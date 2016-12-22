FROM kprpi

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install openjdk-8-jdk jenkins git

COPY jenkins /etc/default/jenkins

EXPOSE 8000

CMD java -jar /usr/share/jenkins/jenkins.war --httpPort=8000
