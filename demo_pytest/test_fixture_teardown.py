#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 6/9/17
"""
import pytest


@pytest.fixture(scope='function')
def teardown_square(request):
    def fin():
        print 'tear down'
        print request.function.result
    request.addfinalizer(fin)


test_data = [
    (2, 4),
    (3, 10),
]


@pytest.mark.parametrize("a,expected", test_data)
def test_square(a, expected, teardown_square):
    test_square.result = a * a
    assert test_square.result == expected
