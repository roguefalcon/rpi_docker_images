#!/usr/bin/python3

from crmapi import app
import os

# By placing our config in ENV variables we can adjust them
# in production with differnet values
# This sets defaults that are good for development
APP_PORT = 5013   # We are using 5013 for the CRMAPI
APP_DEBUG = True

# Now let's see if production wants override them
if 'APP_PORT' in os.environ:
    APP_PORT = int(os.environ['APP_PORT'])

if 'APP_DEBUG' in os.environ and os.environ['APP_DEBUG'] == '0':
    APP_DEBUG = False

app.run(host='0.0.0.0', port=APP_PORT, debug=APP_DEBUG, threaded=True)
