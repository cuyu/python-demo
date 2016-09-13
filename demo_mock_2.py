#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/12/16
"""
from mock import patch, DEFAULT


class Real(object):
    def foo(self):
        return 'foo'

    def bar(self):
        return 'bar'


# Use `patch.object` to replace only one attribute of the object.
# (This function can be also implemented by `patch`, but this is more convenient)
@patch.object(Real, 'foo')
def test_one(mock_foo):
    mock_foo.return_value = 'zzz'
    foo = Real()
    print foo.foo()
    print foo.bar()


real_dict = {'foo': 1, 'bar': 2, 'zzz': 3}


# Use `patch.dict` to 'revise' a dict like object conveniently.
@patch.dict(real_dict, foo=2, bar=3)
def test_two():
    print real_dict


# Use `patch.multiple` to replace several objects in the same module.
@patch.multiple('__main__', real_dict={}, Real=DEFAULT)
def test_three(Real):
    print real_dict
    print Real


if __name__ == '__main__':
    test_one()
    test_two()
    test_three()
