#!/usr/bin/python3

from cc import app
import os

# Define the host and port we want to run on from environment
(HOST, PORT) = os.environ['FLASK_SERVER_NAME'].split(':')

if __name__ == "__main__":

    # Run this app
    app.run(host=HOST, port=PORT, threaded=True)
