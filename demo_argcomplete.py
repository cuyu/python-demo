#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 9/19/16
"""

import readline

def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)


if __name__ == '__main__':
    from argcomplete.completers import EnvironCompleter
    import argparse
    import argcomplete

    parser = argparse.ArgumentParser()
    parser.add_argument("--env-var1").completer = EnvironCompleter
    parser.add_argument("--env-var2").completer = EnvironCompleter
    argcomplete.autocomplete(parser)