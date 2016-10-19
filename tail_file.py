#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simulate Linux command `tail -f`.
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/19/16
"""
import os
import time
import threading


def tail(file_path):
    with open(file_path, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            for line in f:
                print line
            offset = f.tell()
            f.seek(offset)


def write_logs(file_path):
    with open(file_path, 'a') as f:
        while True:
            f.write('bbb\n')
            f.flush()
            time.sleep(1)


if __name__ == '__main__':
    threading.Thread(target=write_logs, args=('/tmp/tail.txt',)).start()
    tail('/tmp/tail.txt')
