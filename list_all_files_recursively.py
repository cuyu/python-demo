#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/27/16
"""
import fnmatch
import os


def list_files(root_path, filter_rule='*'):
    matches = []
    for root, dirnames, filenames in os.walk(root_path):
        for filename in fnmatch.filter(filenames, filter_rule):
            matches.append(os.path.join(root, filename))

    return matches


if __name__ == '__main__':
    print list_files('/tmp')
    print list_files('/tmp', '*.log')
