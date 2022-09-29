#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import *
from fabric.operations import put, run, sudo
import os
from fabric.api import run, local, sudo, env
from datetime import datetime


dt = datetime.now()

env.hosts = ['3.237.41.121', '3.223.3.194']
env.user = 'ubuntu'


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
