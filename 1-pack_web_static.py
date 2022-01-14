#!/usr/bin/python3
'''This module xontents do:pack method'''
from fabric.api import local
from datetime import date, datetime


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
