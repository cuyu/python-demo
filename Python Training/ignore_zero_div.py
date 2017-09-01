#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 8/23/17
"""
from functools import wraps


def ignore_zero_div(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return None

    return wrapper


@ignore_zero_div
def test1():
    1 / 0


@ignore_zero_div
def test2(v1, v2):
    return v1 + v2


@ignore_zero_div
def test3(v1, v2, sep="#"):
    return v1 + sep + v2


@ignore_zero_div
def test4():
    raise ValueError("")


@ignore_zero_div
def test5(v1, v2):
    """this is test4"""
    pass


if __name__ == '__main__':
    assert test1() == None
    assert test2(1, 2) == 3
    assert test3('abc', 'xyz', sep='--') == "abc--xyz"
    assert test3('abc', 'xyz', '--') == "abc--xyz"
    try:
        test4()
        assert False
    except ValueError as ex:
        assert True
    assert test5.__doc__ == "this is test4"
