#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/12/16
"""
from mock import patch

# By default, the patchers recognise methods that start with 'test' as being test methods.
# We set the prefix to `foo` here so that the patch will influence all the methods whose name start with `foo`
patch.TEST_PREFIX = 'foo'
value = 3


@patch('__main__.value', 'not three')
class Thing(object):
    def foo_one(self):
        print value

    def foo_two(self):
        print value

    def bar_one(self):
        print value


if __name__ == '__main__':
    t = Thing()
    t.foo_one()
    t.foo_two()
    t.bar_one()
