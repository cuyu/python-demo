#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/19/16
"""
import pytest

@pytest.fixture(scope='function')
def foo():
    return 'foo'


def test_four(fixture_session, fixture_module, fixture_class, fixture_function, foo):
    assert fixture_session == 'fixture_session'
    assert fixture_module == 'fixture_module'
    assert fixture_class == 'fixture_class'
    assert fixture_function == 'fixture_function'
    assert foo == 'foo'
    assert False
