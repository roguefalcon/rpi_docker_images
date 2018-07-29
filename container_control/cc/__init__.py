from flask import Flask, request, abort

app = Flask(__name__)
app.config.from_envvar('FLASK_CONFIG_FILE')

@app.before_request
def limit_remote_addr():
    whitelist = ['192.168.1.114', '10.136.96.145', '10.136.84.36']
    if request.remote_addr not in whitelist:
        abort(403)  # Forbidden

from cc import control
