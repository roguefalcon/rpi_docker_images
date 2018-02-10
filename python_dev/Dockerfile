FROM kprpi

#RUN apt-get update && apt-get upgrade -y
RUN apt-get update

# Run the debian packages we need
RUN apt-get -y install python python-pip python-dev build-essential openssh-server git libpam-ldapd libnss-ldapd nscd python3 python3-pip python3-dev libffi-dev sqlite3 python3-setuptools nano wget

# Add the python3 packages we need
RUN pip3 install wheel flask bcrypt flake8

# This directory was missing
RUN mkdir /var/run/sshd

# Create a backdoor user
RUN useradd -m -p paUD.XF6AT3SA -s /bin/bash kp

# Custom Configs for HackMT VMs
# We will setup SSH, PAM, LDAP, etc.
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
COPY kenny.vim /usr/share/vim/vim80/colors/kenny.vim
COPY vimrc /etc/vim/vimrc

RUN pam-auth-update --force

# We will expose other ports with the run command
# We always want this port
EXPOSE 22

CMD /tmp/start.sh
