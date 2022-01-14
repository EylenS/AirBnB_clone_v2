#!/usr/bin/python3
'''Deploy web static'''
from fabric.api import local, put, run, env
from datetime import date, datetime
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['34.138.250.25', '50.17.152.241']


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder '''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file = local(
        "tar -cvzf versions/web_static_{}.tgz web_static".format(date))
    if file:
        return ("versions/web_static_{}.tgz web_static".format(date))
    else:
        return None


def do_deploy(archive_path):
    '''This method deployes archive'''
    if exists(archive_path):
        dir = archive_path.split('/')[-1]
        no_tgz = dir.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(path, no_tgz))
        run("tar -xzf /tmp/{} -C {}{}/".format(path, no_tgz))
        run("rm /tmp/{}".format(dir))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_tgz))
        run("rm -rf {}{}/web_static".format(path, no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_tgz))
        return True
    else:
        return False
