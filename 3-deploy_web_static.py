#!/usr/bin/python3
'''Deploy web static'''
from fabric.api import local, put, run, env
from datetime import date, datetime
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['34.138.250.25', '50.17.152.241']


do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    '''creates and distributes an archive to your web servers'''
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
