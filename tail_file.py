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


class NodeLogCollector(object):
    LOG_FILES = frozenset(['audit.log',
                           'metrics.log',
                           'mongod.log',
                           'scheduler.log'])

    def __init__(self, node):
        self.node = node
        self._sftp = self.node.ssh_connection._client.open_sftp()
        self._logs = {}  # A dict to record the collected logs from log files.
        for name in self.LOG_FILES:
            self._logs[name] = []
        self._terminate = False
        self._tail_threads = []

    def __del__(self):
        self._sftp.close()

    def tail_log(self, file_name):
        file_path = os.path.join(self.node.home_path, 'var', 'log', file_name)
        with self._sftp.file(file_path, 'r') as f:
            f.seek(0, os.SEEK_END)
            while not self._terminate:
                for line in f:
                    self._logs[file_name].append((time.time(), line,))
                time.sleep(0.1)
                offset = f.tell()
                f.seek(offset)

    def start_tail_all_logs(self):
        for name in self.LOG_FILES:
            t = threading.Thread(target=self.tail_log, args=(name,))
            self._tail_threads.append(t)
            t.start()

    def stop_tail_all_logs(self):
        self._terminate = True
        for t in self._tail_threads:
            t.join()
