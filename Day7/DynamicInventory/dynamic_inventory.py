#!/usr/bin/python
#Author Jeganathan Swaminathan <jegan@tektutor.org> <http://www.tektutor.org>

import subprocess
import json
from os.path import expanduser

def executeDockerCommand(*args):
    return subprocess.check_output(["docker"] + list(args)).strip()

def docker_inspect(fmt, mcn):
    ip_address = executeDockerCommand("inspect", "-f", fmt, mcn).split()
    return ip_address[0].decode('utf-8')

def docker_port(container_id):
    try:
       published_port = executeDockerCommand("port", container_id, "22").split()
       published_port = published_port[0].decode('utf-8')
       tokens = published_port.split(':')
       return tokens[1]
    except:
       return "22"

def get_host_vars(container_id):
    home = expanduser("~")
    ip = [docker_inspect("{{.NetworkSettings.IPAddress}}", container_id)]

    publishedPort = docker_port(container_id)

    ssh_vars = {
        "ansible_port": publishedPort,
        "ansible_private_key_file": home+ "/.ssh/" + "id_rsa",
        "ansible_user": "root",
        "ansible_become_user": "root",
        "ansible_become_password": "root",
    }

    if ( publishedPort == "22" ):
        ssh_vars.update({"ansible_host": docker_inspect("{{.NetworkSettings.IPAddress}}", container_id) })
    else:
        ssh_vars.update({"ansible_host": "localhost"})

    hostConnectionDetails = {"hosts": ip, "vars": ssh_vars}
    return hostConnectionDetails

class DockerInventory():
      def __init__(self):
          self.inventory = {} # Ansible Inventory
          containers_ids = executeDockerCommand("ps", "-q").splitlines()
          json_data = {m.decode("utf-8"): get_host_vars(m.decode("utf-8")) for m in containers_ids}
          print ( json.dumps(json_data,indent=4,sort_keys=True) )
            
DockerInventory()
