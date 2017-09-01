#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/28/16
"""
import sys
print sys.stdout.encoding # UTF-8
print u'ü' #
    # print repr(unicode('得', 'utf-8')), repr(u'得'), repr('得'), repr('得'.decode('utf-8'))
    # print '\xe2\xa4\xb4'.decode('utf-8')
    # print u'\u2934'.encode('utf-8')
