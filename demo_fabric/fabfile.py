#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/22/16
"""
from fabric.api import *

env.roledefs = {
    'systest': [
        'root@systest-auto-deployer:22',
        'root@systest-auto-idx5:22', ]
}

# The key in `env.passwords` must be the same to the defined hosts (and must contains the username and port)
env.passwords = {
    'root@systest-auto-deployer:22': 'sp1unk',
    'root@systest-auto-idx5:22': 'sp1unk',
}


@parallel
@roles('systest')
def echo():
    run('ls /root')
