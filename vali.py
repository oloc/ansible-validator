#!/usr/bin/env python
#
# Olivier Locard

import json, os
from docker import Client

DockerFileDir = './dockerfiles'

cli = Client(base_url='unix://var/run/docker.sock')


def pull(distribution, version):
    for line in cli.pull(distribution + ':' + version, stream=True):
        print(json.dumps(json.loads(line), indent=5))


def dck_build(distribution, version):
    image = distribution + '-' + version
    dockerfile = DockerFileDir + '/' + image

    f = open(dockerfile, 'r')
    response = [line for line in cli.build(fileobj=f, tag=image + ':ansible', )]

    return response

def dck_run(image):
    cmd='/sbin/init'

    container = cli.create_container(image=image, detach=True, volumes=os.getcwd()+":/etc/ansible/roles/role_under_test:ro", command=cmd)
    cli.start(container=container.get('Id'))

    return container

def dck_exec(container,test):
    response = cli.exec_create(container=container, tty=True, cmd='ansible-playbook /etc/ansible/roles/role_under_test/tests/'+test)
    
    return response

print (dck_build('debian','8'))
#print (dck_run("debian-8:ansible"))

print(dck_exec(dck_run("debian-8:ansible"),'test.yml --syntax-check'))
