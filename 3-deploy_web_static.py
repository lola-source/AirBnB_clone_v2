#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.operations import put, run, sudo
import os
from fabric.api import run, local, sudo, env
from datetime import datetime


dt = datetime.now()

env.hosts = ['3.237.41.121', '3.223.3.194']

