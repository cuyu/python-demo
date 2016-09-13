#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/12/16
"""

from mock import patch


class Foo(object):
    def print_foo(self):
        return 'foo'


def some_function():
    instance = Foo()
    print instance
    return instance.print_foo()


if __name__ == '__main__':
    # Will create a MagicMock object to replace class `Foo`
    with patch('__main__.Foo') as MockFoo:
        # Call the MagicMock object will return a new MagicMock object and is bounded with the calling MockFoo()
        # (means each time you call MockFoo()/Foo(), will return the same MagicMock object)
        mock_instance = MockFoo.return_value
        # Set the print_foo()'s return value to 'bar'
        mock_instance.print_foo.return_value = 'bar'
        print mock_instance
        # Call the function which calls Foo.print_foo(), this actually calls the mock_instance.print_foo()
        result = some_function()
        assert result == 'bar'
