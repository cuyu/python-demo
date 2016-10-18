#!/usr/bin/env python

import os
import sys
from collections import namedtuple
from copy import deepcopy

from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor


def run_playbook(playbook_path, host_list_path):
    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=host_list_path)

    if not os.path.exists(playbook_path):
        print '[INFO] The playbook does not exist'
        sys.exit()

    Options = namedtuple('Options',
                         ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection', 'module_path', 'forks',
                          'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args',
                          'sftp_extra_args', 'scp_extra_args', 'become', 'become_method', 'become_user',
                          'verbosity', 'check'])
    options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                      module_path=None,
                      forks=100, remote_user='slotlocker', private_key_file=None, ssh_common_args=None,
                      ssh_extra_args=None,
                      sftp_extra_args=None, scp_extra_args=None, become=True, become_method=None, become_user='root',
                      verbosity=None, check=False)

    variable_manager.extra_vars = {'hosts': 'mywebserver'}  # This can accomodate various other command line arguments.`

    passwords = {}

    pbex = PlaybookExecutor(playbooks=[playbook_path], inventory=inventory,
                            variable_manager=variable_manager,
                            loader=loader, options=options, passwords=passwords)

    results = pbex.run()

    node_info = dict()
    host_vars = pbex._tqm.hostvars
    for info in host_vars._cached_result.values():
        node_info[info['ansible_nodename']] = deepcopy(info)
    return results, node_info


if __name__ == '__main__':
    results, node_info = run_playbook('/Users/CYu/Code/Python/python-demo/demo_ansible/playbook.yml',
                                      '/Users/CYu/Code/Python/python-demo/demo_ansible/hosts')
    print '----------Below is my print out-----------'
    for name in node_info:
        print name + '  stdout:' + '\n'
        for line in node_info[name]['out']['stdout_lines']:
            print line + '\n'
