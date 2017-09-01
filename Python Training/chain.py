#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/23/17
"""

class ChainIterator(object):
    def __init__(self, *list_of_iterable):
        self.list_of_iterable = list_of_iterable
        self.index = 0  # The position of current iterator in list_of_iterable
        self.current_iter = iter(self.list_of_iterable[self.index])

    def __iter__(self):
        self.index = 0
        self.current_iter = iter(self.list_of_iterable[self.index])
        return self

    def next(self):
        try:
            value = next(self.current_iter)
            return value
        except StopIteration:
            if self.index == len(self.list_of_iterable) - 1:
                raise
            else:
                self.index += 1
                self.current_iter = iter(self.list_of_iterable[self.index])
                return self.next()


def chain(*list_of_iterable):
    """
    accepts multiple iterable/iterator and return an iterator to chain them
    Usage and test:
    assert list(chain(xrange(1,6,2), "abc", [2,3,4])) == [1,3,5,'a','b','c',2,3,4]

    assert list(chain(xrange(1,10,2), xrange(10,14))) == [1,3,5,7,9,10,11,12,13]

    Memory usage:
    please use memory at O(1) complexity.

    Plus if support:
    c = chain(xrange(1,10,2), xrange(10,14))
    assert list(c) == [1,3,5,7,9,10,11,12,13]
    assert list(c) == [1,3,5,7,9,10,11,12,13]
    """
    return ChainIterator(*list_of_iterable)


if __name__ == '__main__':
    assert list(chain(xrange(1, 6, 2), "abc", [2, 3, 4])) == [1, 3, 5, 'a', 'b', 'c', 2, 3, 4]
    assert list(chain(xrange(1, 10, 2), xrange(10, 14))) == [1, 3, 5, 7, 9, 10, 11, 12, 13]
    c = chain(xrange(1,10,2), xrange(10,14))
    assert list(c) == [1,3,5,7,9,10,11,12,13]
    assert list(c) == [1,3,5,7,9,10,11,12,13]