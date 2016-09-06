#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/5/16
"""
from multiprocessing import Process
import signal
import time


class TerminateInterrupt(BaseException): pass


def signal_handler(signum, stack):
    print 'Capture terminate signal.'
    raise TerminateInterrupt


class MyProcess(Process):
    def __init__(self):
        super(MyProcess, self).__init__()
        self.a = 0

    def run(self):
        signal.signal(signal.SIGTERM, signal_handler)
        try:
            while True:
                self.a += 1
                time.sleep(1)
        except TerminateInterrupt:
            print 'Exit the process.'


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    time.sleep(5)
    p.terminate()
    p.join()
