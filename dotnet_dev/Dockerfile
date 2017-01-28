FROM armv7/armhf-ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install build-essential openssh-server git libpam-ldapd libnss-ldapd nscd curl libunwind8 gettext wget libunwind8-dev libicu-dev liblttng-ust-dev libcurl4-openssl-dev libssl-dev uuid-dev vim sudo

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

RUN pam-auth-update --force

# Install .Net Core
COPY dotnet-ubuntu.16.04-arm.1.2.0-beta-001291-00.tar.gz /tmp/dotnet_ubuntu_arm.tar.gz
RUN tar zxvf /tmp/dotnet_ubuntu_arm.tar.gz
RUN cp /dotnet /bin/dotnet
RUN cp /host/fxr/1.2.0-beta-001291-00/libhostfxr.so /bin/.
RUN cp -r /host /bin/.
RUN cp -r /shared /bin/.

# Set the prompt to match the vm
ENV PS1 '\[\033[0;32m\]\u@\h:\[\033[36m\]\W\[\033[0m\]# '

EXPOSE 22

CMD /tmp/start.sh
