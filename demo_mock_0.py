#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/12/16
"""

from mock import MagicMock

if __name__ == '__main__':
    # MagicMock object will generate a new MagicMock object if you visit to a undefined attribute.
    m0 = MagicMock()
    print m0.aaa

    # You can define some attributes in the construct function of MagicMock conveniently.
    m1 = MagicMock(aaa=1, bbb=2)
    print m1.aaa, m1.bbb
    # By `del` method, you can delete an attribute of MagicMock object, and it will cause AttributeError when you visit the deleted attribute.
    del m1.ccc
    try:
        print m1.ccc
    except AttributeError, e:
        print 'AttributeError'

    # Use spec to limit a set of attributes, will cause AttributeError when you visit attribute out of the spec list.
    m2 = MagicMock(spec=['aaa', 'bbb'])
    print m2.aaa
    try:
        print m2.ccc
    except AttributeError, e:
        print 'AttributeError'

    # Use spec to input a object can make the MagicMock object pass `isinstance` test.
    dd = dict()
    m3 = MagicMock(spec=dd)
    print isinstance(m3, dict)

    # Set the `return_value` to a MagicMock object will let the calling of the object always return the same value.
    m4 = MagicMock()
    m4.return_value = 6
    print m4(4, 'aaa'), m4([1,2,3])

    # Use side_effect to bind a method to the MagicMock object so that it can return different values according to the inputs.
    m4 = MagicMock(side_effect=lambda value: value * 2)
    print m4(3), m4('abc')

    # Can also bind a iterable object to side_effect. In this case, the return value will be the traversal of the iterable object.
    # And has nothing to do with the inputs.
    m5 = MagicMock()
    m5.side_effect = [5, 'hi']
    print m5(2), m5()
