#!/bin/bash

rm -rf web
git clone bill@192.168.3.51:/srv/git/web.git

rm -rf crm
git clone bill@192.168.3.51:/srv/git/crm.git

rm -rf crmapi
git clone bill@192.168.3.51:/srv/git/crmapi.git

rm -rf ops
git clone bill@192.168.3.51:/srv/git/ops.git

rm -rf opsapi
git clone bill@192.168.3.51:/srv/git/opsapi.git

rm -rf mobileapi
git clone bill@192.168.3.51:/srv/git/mobileapi.git

rm -rf mobileapi
git clone bill@192.168.3.51:/srv/git/mobileapi.git

scp -r * rogue@192.168.1.137:/tmp/hackmt/.
