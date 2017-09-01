#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/23/17
"""
from functools import wraps


def ignore_zero_div(ret_value=None):
    """
    same as ignore_zero_div, ignore ZeroDivisionError if any. return passed ret_value instead of None by default.

    Usage and test:

    ((same as ignore_zero_div, but add feature as below))

    @ignore_zero_div(ret_value="abc")
    def test1():
          1/0

    assert test1() == "abc"

    @ignore_zero_div()
    def test2():
          1/0

    assert test1() == None
    """

    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except ZeroDivisionError:
                return ret_value

        return wrapper

    return deco


@ignore_zero_div(ret_value="abc")
def test1():
    1 / 0


@ignore_zero_div()
def test2():
    1 / 0


if __name__ == '__main__':
    assert test1() == "abc"
    assert test2() == None
