#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/21/16
"""
import threading

LARGE_NUMBER = 1000000 * 100


def func():
    for i in range(LARGE_NUMBER):
        pass


def func2():
    for i in range(2):
        func()


def func3():
    result = []
    a = 0
    for i in range(LARGE_NUMBER):
        a += i
    result.append(a)


@profile
def main():
    t = threading.Thread(target=func)
    t2 = threading.Thread(target=func2)
    t3 = threading.Thread(target=func3)

    t.start()
    t2.start()
    t3.start()

    t.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    main()
