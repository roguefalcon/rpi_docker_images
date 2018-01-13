#!/usr/bin/python3

from myapp import app

# Define the port we want to run on
PORT = 5001

# Run this app
app.run(debug=True, host='0.0.0.0', port=PORT, threaded=True)
