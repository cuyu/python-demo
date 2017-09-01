#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/23/17
"""
class DedupIterator(object):
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter = iter(iterable)
        self._map = set()

    def __iter__(self):
        self.iter = iter(self.iterable)
        self._map = set()
        return self

    def next(self):
        value = next(self.iter)
        if value in self._map:
            return self.next()
        else:
            self._map.add(value)
            return value


def dedup(iterable):
    """accept an iterable/iterator and return the unique value once

    Usage and test:
    assert list(dedup([1,2,3,3,2,1,4])) == [1,2,3,4]
    assert list(dedup("aaaaa")) == ['a']
    assert list(dedup("abbbbbb")) == ['a','b']

    Performance:
    Memory: totally O(N) is OK
    Time: O(1) for each element (totally O(N) to iterating whole target)

    Plus if support:
    c = dedup([1,2,3,3,2,1,4])
    assert list(c) == [1,2,3,4]
    assert list(c) == [1,2,3,4]
    """
    return DedupIterator(iterable)


if __name__ == '__main__':
    assert list(dedup([1,2,3,3,2,1,4])) == [1,2,3,4]
    assert list(dedup("aaaaa")) == ['a']
    assert list(dedup("abbbbbb")) == ['a','b']
    c = dedup([1,2,3,3,2,1,4])
    assert list(c) == [1,2,3,4]
    assert list(c) == [1,2,3,4]
