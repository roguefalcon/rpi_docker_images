FROM kprpi

RUN apt-get -y update && apt-get -u upgrade

RUN apt-get -y install python python-pip python-dev build-essential openssh-server git

RUN pip install Flask
RUN pip install tinydb

RUN mkdir /var/run/sshd

RUN useradd -m -p paUD.XF6AT3SA -s /bin/bash kp

COPY sshd_config /etc/ssh/sshd_config
COPY motd /etc/motd
COPY issue.net /etc/issue.net

EXPOSE 22

CMD /usr/sbin/sshd -D
