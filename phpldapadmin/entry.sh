#!/bin/bash

set -e

openvpn --daemon --config phpldapadmin.ovpn
sleep 25

exec "$@"
