FROM kprpi

RUN apt-get -y update && apt-get -u upgrade

RUN apt-get -y install python python-pip python-dev build-essential

RUN pip install Flask
RUN pip install tinydb

RUN apt-get -y install openssh-server

RUN mkdir /var/run/sshd

RUN useradd -m -p paUD.XF6AT3SA -s /bin/bash kp

EXPOSE 22

CMD /usr/sbin/sshd -D
