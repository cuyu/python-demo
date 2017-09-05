#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def demo(func, *input):
    return func(*input)


if __name__ == '__main__':
    print demo(lambda input: input + 1, 1)
    print demo(lambda a, b: a + b, 1, 2)
    print demo(lambda name: os.path.isdir(os.path.join('/tmp', name)), 'abc')
