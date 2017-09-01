#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/11/17
"""


def deco(n):
    def inner_decorator(f):
        print n, 'inner'

        def wrapper():
            print n, f.__name__
            f()

        return wrapper

    return inner_decorator


def deco2(f):
    print 'inner', f.__name__

    def wrapper():
        print f.__name__
        f()

    return wrapper


@deco2
@deco2
def demo():
    print 'hello world'


if __name__ == '__main__':
    # deco(n=1)(deco(n=2)(demo))()
    # deco2(deco2(demo))()
    demo()
