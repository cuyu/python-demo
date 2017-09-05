#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/19/16
"""

# import readline
#
# def completer(text, state):
#     options = [i for i in commands if i.startswith(text)]
#     if state < len(options):
#         return options[state]
#     else:
#         return None
#
# readline.parse_and_bind("tab: complete")
# readline.set_completer(completer)


#################################################################
# To register with argcompletion, run following command:        #
#   eval "$(register-python-argcomplete demo_argcomplete.py)"   #
#################################################################
def MyCompleter(prefix, **kwargs):
    results = ['aaa', 'bbb']
    return (c for c in results if c.startswith(prefix))

if __name__ == '__main__':
    import argparse
    import argcomplete
    import sys

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    create_parser = subparsers.add_parser('new')
    create_parser.add_argument('title')
    create_parser.add_argument('category').completer = MyCompleter
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    line = sys.stdin.readline()
    print line, args
