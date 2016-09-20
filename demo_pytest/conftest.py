#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/19/16
"""

import pytest


@pytest.fixture(scope='session')
def fixture_session():
    print 'fixture_session tear up'
    yield 'fixture_session'
    print 'fixture_session tear down'


@pytest.fixture(scope='module')
def fixture_module():
    print 'fixture_module tear up'
    yield 'fixture_module'
    print 'fixture_module tear down'


@pytest.fixture(scope='class')
def fixture_class():
    print 'fixture_class tear up'
    yield 'fixture_class'
    print 'fixture_class tear down'


@pytest.fixture(scope='function')
def fixture_function(request):
    print 'fixture_function tear up'

    def fin():
        print 'fixture_function tear down'

    request.addfinalizer(fin)
    return 'fixture_function'


@pytest.fixture(scope='function')
def fixture_autouse():
    print 'fixture_autouse tear up'
    yield
    print 'fixture_autouse tear down'
