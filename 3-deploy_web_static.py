#!/usr/bin/python3
'''Deploy web static'''
from fabric.api import local, put, run, env
from datetime import date, datetime
from os.path import exists, getsize


env.user = 'ubuntu'
env.hosts = ['34.138.250.25', '50.17.152.241']


def do_pack():
    '''generates a .tgz archive from the contents of the web_static folder '''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
    archive_path = "versions/web_static_{}.tgz".format(date)
    if exists(archive_path) and getsize(archive_path) > 0:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    '''This method deployes archive'''
    if exists(archive_path):
        dir_ex = archive_path.split('/')[-1]
        no_tgz = dir_ex.split('.')[0]
        path = "/data/web_static/releases/"
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # make sure the directory is there
        run("mkdir -p {}{}/".format(path, no_tgz))
        # Uncompress the archive to the folder /data/web_static/releases/
        run("tar -xzf /tmp/{} -C {}{}/".format(dir_ex, path, no_tgz))
        # Delete the archive from the web server
        run("rm /tmp/{}".format(dir_ex))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_tgz))
        run("rm -rf {}{}/web_static".format(path, no_tgz))
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link
        run("ln -s {}{}/ /data/web_static/current".format(path, no_tgz))
        return True
    else:
        return False


def deploy():
    '''creates and distributes an archive to your web servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
