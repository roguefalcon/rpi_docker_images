#!/bin/sh

echo "******************************"
echo "**** POSTFIX STARTING UP *****"
echo "******************************"

# Make and reown postfix folders
mkdir -p /var/spool/postfix/ && mkdir -p /var/spool/postfix/pid
chown root: /var/spool/postfix/
chown root: /var/spool/postfix/pid

# Disable SMTPUTF8, because libraries (ICU) are missing in alpine
postconf -e smtputf8_enable=no

# Update aliases database. It's not used, but postfix complains if the .db file is missing
postalias /etc/postfix/aliases

# Disable local mail delivery
postconf -e mydestination=
# Don't relay for any domains
postconf -e relay_domains=

# As this is a server-based service, allow any message size -- we hope the server knows
# what it is doing
postconf -e "message_size_limit=0"

# Reject invalid HELOs
postconf -e smtpd_delay_reject=yes
postconf -e smtpd_helo_required=yes
postconf -e "smtpd_helo_restrictions=permit_mynetworks,reject_invalid_helo_hostname,permit"

# Set up host name
if [ ! -z "$HOSTNAME" ]; then
	postconf -e myhostname="$HOSTNAME"
else
	postconf -# myhostname
fi

# Set up a relay host, if needed
if [ ! -z "$RELAYHOST" ]; then
	echo -n "- Forwarding all emails to $RELAYHOST"
	postconf -e relayhost=$RELAYHOST

	if [ -n "$RELAYHOST_USERNAME" ] && [ -n "$RELAYHOST_PASSWORD" ]; then
		echo " using username $RELAYHOST_USERNAME."
		echo "$RELAYHOST $RELAYHOST_USERNAME:$RELAYHOST_PASSWORD" >> /etc/postfix/sasl_passwd
		postmap hash:/etc/postfix/sasl_passwd
		postconf -e "smtp_sasl_auth_enable=yes"
		postconf -e "smtp_sasl_password_maps=hash:/etc/postfix/sasl_passwd"
		postconf -e "smtp_sasl_security_options=noanonymous"
	else
		echo " without any authentication. Make sure your server is configured to accept emails coming from this IP."
	fi
else
	echo "- Will try to deliver emails directly to the final server. Make sure your DNS is setup properly!"
	postconf -# relayhost
	postconf -# smtp_sasl_auth_enable
	postconf -# smtp_sasl_password_maps
	postconf -# smtp_sasl_security_options
fi

if [ ! -z "$MYNETWORKS" ]; then
	postconf -e mynetworks=$MYNETWORKS
else
	postconf -e "mynetworks=127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16"
fi

# Split with space
if [ ! -z "$ALLOWED_SENDER_DOMAINS" ]; then
	echo -n "- Setting up allowed SENDER domains:"
	allowed_senders=/etc/postfix/allowed_senders
	rm -f $allowed_senders $allowed_senders.db > /dev/null
	touch $allowed_senders
	for i in $ALLOWED_SENDER_DOMAINS; do
		echo -n " $i"
		echo -e "$i\tOK" >> $allowed_senders
	done
	echo
	postmap $allowed_senders

	postconf -e "smtpd_restriction_classes=allowed_domains_only"
	postconf -e "allowed_domains_only=permit_mynetworks, reject_non_fqdn_sender reject"
#   Update: loosen up on RCPT checks. This will mean we might get some emails
#           which are not valid, but the service connecting will be able to
#           send out emails much faster, as there will be no lookup and lockup
#           if the target server is not responding or available
#	postconf -e "smtpd_recipient_restrictions=reject_non_fqdn_recipient, reject_unknown_recipient_domain, reject_unverified_recipient, check_sender_access hash:$allowed_senders, reject"
	postconf -e "smtpd_recipient_restrictions=reject_non_fqdn_recipient, reject_unknown_recipient_domain, check_sender_access hash:$allowed_senders, reject"
else
	postconf -# "smtpd_restriction_classes"
#   Update: loosen up on RCPT checks. This will mean we might get some emails
#           which are not valid, but the service connecting will be able to send
#           out emails much faster, as there will be no lookup and lockup if the
#           target server is not responding or available
#	postconf -e "smtpd_recipient_restrictions=reject_non_fqdn_recipient,reject_unknown_recipient_domain,reject_unverified_recipient"
	postconf -e "smtpd_recipient_restrictions=reject_non_fqdn_recipient, reject_unknown_recipient_domain, defer_unauth_destination, permit"
fi

# Kenny added these lines trying to get mail to relay
postconf -# "smtpd_restriction_classes"
postconf -e "smtpd_recipient_restrictions=reject_non_fqdn_recipient, reject_unknown_recipient_domain, defer_unauth_destination, permit"

# Since we are behind closed doors, let's just permit all relays.
postconf -e "smtpd_relay_restrictions=permit"

# Setup Pyatt Dev Training relay
postconf -e "virtual_alias_domains=pyattdevtraining.com"
postconf -e "virtual_alias_maps=hash:/etc/postfix/virtual"
postmap /etc/postfix/virtual

# Use 587 (submission)
sed -i -r -e 's/^#submission/submission/' /etc/postfix/master.cf

if [ -d /docker-init.db/ ]; then
	echo "- Executing any found custom scripts..."
	for f in /docker-init.db/*; do
		case "$f" in
			*.sh)     chmod +x "$f"; echo -e"\trunning $f"; . "$f" ;;
			*)        echo "$0: ignoring $f" ;;
		esac
	done
fi

echo "- Staring rsyslog and postfix"
exec supervisord -c /etc/supervisord.conf

