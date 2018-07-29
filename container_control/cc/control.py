from flask import request, jsonify
from cc import app
import docker


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
# a bash script and just run it
