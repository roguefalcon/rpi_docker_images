<?php
/**
 * Dokuwiki's Main Configuration File - Local Settings
 * Auto-generated by Debian postinst script
 */

$conf['title'] = 'HackMT DokuWiki';
$conf['license'] = 'cc-by-sa';
#$conf['lang'] = 'en';
$conf['useacl'] = 1;
$conf['openregister']=0;
$conf['authtype']    = 'ldap';
$conf['auth']['ldap']['server']      = 'ldap://ldap.pyatt.lan:389';
$conf['auth']['ldap']['usertree']    = 'ou=People, dc=pyatt, dc=lan';
$conf['auth']['ldap']['grouptree']   = 'ou=Group, dc=pyatt, dc=lan';
$conf['auth']['ldap']['userfilter']  = '(&(uid=%{user})(objectClass=posixAccount))';
$conf['auth']['ldap']['groupfilter'] = '(&(objectClass=posixGroup)(|(gidNumber=%{gid})(memberUID=%{user})))';

# This is optional but may be required for your server:
$conf['auth']['ldap']['version']    = 3;
$conf['auth']['ldap']['debug']      = 0;

$conf['superuser'] = '@admin';

