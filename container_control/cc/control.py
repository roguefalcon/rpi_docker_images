from flask import request, jsonify, send_from_directory
from cc import app
import docker
import os


# List of containers ==========================================================
@app.route('/1.0/containers')
def container_list():

    # Local Vars
    response = {}
    response['containers'] = []

    # Use the docker module to get a list of running containers
    client = docker.from_env()
    for container in client.containers.list():
        response['containers'].append(container.name)

    return jsonify(response)


# Find specific Container =====================================================
@app.route('/1.0/containers/<vm_name>')
def find_container(vm_name):

    # Local Vars
    response = {}

    # Use the docker module to get a list of running containers
    client = docker.from_env()
    for container in client.containers.list():
        if container.name == vm_name:
            response[vm_name] = 'Running'

    return jsonify(response)


# Start Container =============================================================
@app.route('/1.0/containers/<vm_name>/start')
def start_container(vm_name):

    # Local Vars
    response = {}

    # Use the docker module to get a list of running containers
    client = docker.from_env()
    mv_vm = client.containers.get(vm_name)
    success = mv_vm.start()
    response[vm_name] = 'Running'

    # Let them know it worked
    return jsonify(response)


# Stop Container ==============================================================
@app.route('/1.0/containers/<vm_name>/stop')
def stop_container(vm_name):

    # Local Vars
    response = {}

    # Use the docker module to get a list of running containers
    client = docker.from_env()
    mv_vm = client.containers.get(vm_name)
    success = mv_vm.stop()
    response[vm_name] = 'Stopped'

    # Let them know it worked
    return jsonify(response)


# Create Container ============================================================
# This one isn't as simple since I need to do a bunch of things so I created
# a bash script and just run it.  It creates keys, sets up OpenVPN, makes
# a Docker image (with Dockerfile) and then runs the container
@app.route('/1.0/containers/create')
def create_container():

    # Setup the response
    response = {}
    response['success'] = 'false'

    # URL Params
    vm_name = request.args.get('vm_name')
    ip_addr = request.args.get('ip')
    username = request.args.get('username')
    password = request.args.get('password')

    # There is a shell script that does the heavy lifting so we will call it with the args it expects
    create_vm = os.popen("/root/create_dev_container.sh " + vm_name + " " + ip_addr + " " + password + " " + username).readlines()
    if create_vm:
        response['success'] = 'true'

    # Report success (good or bad)
    return jsonify(response)


# Create OpenVPN File =========================================================
@app.route('/1.0/create_ovpn')
def create_ovpn():

    # Setup the response
    response = {}
    response['success'] = 'false'

    username = request.args.get('username')
    create_vm = os.popen("/root/generate_ovpn.sh " + username).readlines()
    if create_vm:
        response['success'] = 'true'

    # Report success (good or bad)
    return jsonify(response)


# Download OpenVPN File =======================================================
@app.route('/1.0/download_ovpn')
def download_ovpn():

    username = request.args.get('username')
    if username:
        return send_from_directory('/root', username + ".ovpn", as_attachment=True)
