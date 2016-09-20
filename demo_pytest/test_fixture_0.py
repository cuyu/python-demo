#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/19/16
"""

import pytest


@pytest.mark.usefixtures('fixture_autouse')
class TestFixtureScope(object):
    def test_one(self, fixture_session, fixture_module, fixture_class, fixture_function):
        assert fixture_session == 'fixture_session'
        assert fixture_module == 'fixture_module'
        assert fixture_class == 'fixture_class'
        assert fixture_function == 'fixture_function'
        assert False

    def test_two(self, fixture_session, fixture_module, fixture_class, fixture_function):
        assert fixture_session == 'fixture_session'
        assert fixture_module == 'fixture_module'
        assert fixture_class == 'fixture_class'
        assert fixture_function == 'fixture_function'
        assert False


def test_three(fixture_session, fixture_module, fixture_class, fixture_function):
    assert fixture_session == 'fixture_session'
    assert fixture_module == 'fixture_module'
    assert fixture_class == 'fixture_class'
    assert fixture_function == 'fixture_function'
    assert False
