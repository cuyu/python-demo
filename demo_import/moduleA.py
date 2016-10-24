#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/24/16
"""
import moduleB


def setA(a):
    moduleB.A = a


if __name__ == '__main__':
    setA('aaa')
    moduleB.printA()
    moduleB.setA('bbb')
    moduleB.printA()
