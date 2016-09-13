#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/7/16
"""

import socket


def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, port))
    if result == 0:
        print 'socket is open'
    else:
        print 'socket is not open'
    s.close()


if __name__ == '__main__':
    check_port('datapump4', 2181)
