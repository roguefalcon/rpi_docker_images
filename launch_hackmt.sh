#!/bin/bash

# Launch git repos
nohup git daemon --reuseaddr --export-all --verbose --enable=receive-pack --base-path=/opt/git /opt/git > git.daemon.out &
