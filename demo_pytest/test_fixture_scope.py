#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 6/9/17
"""
import pytest

INDEX_A = 0
INDEX_B = 0


@pytest.fixture(scope='function')
def fixture_a():
    global INDEX_A
    INDEX_A += 1
    return INDEX_A


@pytest.fixture(scope='module')
def fixture_b():
    global INDEX_B
    INDEX_B += 1
    return INDEX_B


@pytest.mark.usefixtures('fixture_a', 'fixture_b')
def test_1():
    assert INDEX_A == 1
    assert INDEX_B == 1


@pytest.mark.usefixtures('fixture_a', 'fixture_b')
def test_2():
    assert INDEX_A == 2
    assert INDEX_B == 2  # Will fail cause fixture will not be called again as its scope is module even we use `usefixtures` explicitly!
