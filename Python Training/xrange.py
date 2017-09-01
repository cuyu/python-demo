#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/23/17
"""
class XrangeIterator(object):
    def __init__(self, start, stop=None, step=1):
        if stop:
            self.start = start
            self.stop = stop
        else:
            self.start = 0
            self.stop = start
        self.step = step
        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def next(self):
        if self.step > 0:
            condition = self.current < self.stop
        else:
            condition = self.current > self.stop
        if condition:
            value = self.current
            self.current += self.step
            return value
        else:
            raise StopIteration


def xrange(start, stop=None, step=1):
    """
    Return a iterator containing an arithmetic progression of integers.
    xrange(i, j) returns i, i+1, i+2, ..., j-1 on demand; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns 0, 1, 2, 3. The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

    Usage and test:
    assert list(xrange(4)) == [0,1,2,3]
    assert list(xrange(1,4)) == [1,2,3]
    assert list(xrange(2,10,2)) == [2,4,6,8]
    assert list(xrange(10,6,-1)) == [10,9,8,7]
    assert list(xrange(10,6,-2)) == [10,8]

    Memory usage:
    please use memory at O(1) complexity.

    Plus if support:
    c = xrange(4)
    assert list(c) == [0,1,2,3]
    assert list(c) == [0,1,2,3]
    """
    return XrangeIterator(start, stop, step)


if __name__ == '__main__':
    assert list(xrange(4)) == [0, 1, 2, 3]
    assert list(xrange(1,4)) == [1,2,3]
    assert list(xrange(2,10,2)) == [2,4,6,8]
    assert list(xrange(10,6,-1)) == [10,9,8,7]
    assert list(xrange(10,6,-2)) == [10,8]
    c = xrange(4)
    assert list(c) == [0,1,2,3]
    assert list(c) == [0,1,2,3]