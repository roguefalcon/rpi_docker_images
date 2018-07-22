#!/bin/sh

set -e

# When not limiting the open file descritors limit, the memory consumption of
# slapd is absurdly high. See https://github.com/docker/docker/issues/8231
ulimit -n 8192

openvpn --daemon --config ldap.ovpn
sleep 25

exec "$@"
