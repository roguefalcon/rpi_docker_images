#!/usr/bin/python

import sys, os

if len(sys.argv) < 2:
   print "USAGE: build_dev_vm.py [hostname] [docker_image]"
   print "  example: ./build_dev_vm.py blue.pyatt.lan python_dev"

print "Building vm for host", sys.argv[1], "with image", sys.argv[2]

os.system("nslookup " + str(sys.argv[1]) + " | grep Address | grep -v '#53' | awk '{print $2}' > /tmp/kpout")

with open('/tmp/kpout') as f:
   lines = f.readlines()

ip = lines[0].rstrip()
print "Found IP Address:", ip

print "docker run --name " + sys.argv[1] + " -d --restart always -p " + ip + ":22:22 -p " + ip + ":80:80 -p " + ip + ":5000:5000 -h " + sys.argv[1] + " " + sys.argv[2] 
