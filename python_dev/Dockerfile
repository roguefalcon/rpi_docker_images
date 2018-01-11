FROM kprpi

#RUN apt-get update && apt-get upgrade -y
RUN apt-get update

RUN apt-get -y install python python-pip python-dev build-essential openssh-server git libpam-ldapd libnss-ldapd nscd python3 python3-pip python3-dev libffi-dev sqlite3 python3-setuptools nano wget

RUN pip3 install wheel flask bcrypt flake8
#RUN pip3 install sqlite3

RUN mkdir /var/run/sshd

RUN useradd -m -p paUD.XF6AT3SA -s /bin/bash kp

COPY sshd_config /etc/ssh/sshd_config
COPY motd /etc/motd
COPY issue.net /etc/issue.net
COPY common-session /etc/pam.d/common-session
COPY start.sh /tmp/start.sh
RUN chmod u+x /tmp/start.sh
COPY nslcd.conf /etc/nslcd.conf
RUN chmod 600 /etc/nslcd.conf
COPY pam_ldap.conf /etc/pam_ldap.conf
COPY ldap.conf /etc/ldap/ldap.conf
COPY sudoers /etc/sudoers
COPY nsswitch.conf /etc/nsswitch.conf
COPY defaults.vim /usr/share/vim/vim80/defaults.vim

RUN pam-auth-update --force

EXPOSE 22

CMD /tmp/start.sh
