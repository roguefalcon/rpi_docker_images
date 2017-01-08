#!/bin/bash

ansible -m command -a "uptime" container-servers
ansible -m command -a "free -mt" container-servers
