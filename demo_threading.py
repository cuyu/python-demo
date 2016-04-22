#!/usr/bin/python

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.delay, 5)
        print "Exiting " + self.name


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


if __name__ == '__main__':
    # Create new threads
    thread1 = MyThread("Thread-1", 1)
    thread2 = MyThread("Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

    print "Exiting Main Thread"

# >See produce_consume.py for more info.
