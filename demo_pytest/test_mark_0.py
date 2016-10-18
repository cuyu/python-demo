#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/20/16
"""
import pytest

MyTest = pytest.mark.mytest


class MyTestType:
    new_test = "new_test"
    old_test = "old_test"
    not_run = "not_run"


@MyTest(test_type=MyTestType.old_test)
def test_one():
    assert False


@MyTest(test_type=MyTestType.new_test)
def test_two():
    assert False


@MyTest(test_type=MyTestType.not_run)
def test_three():
    assert False
