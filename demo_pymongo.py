#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 10/25/16
"""

from pymongo import MongoClient


class MongoHelper(object):
    def __init__(self, db_name):
        self.client = MongoClient("localhost:27017")
        self.db = self.client[db_name]

    def insert_document(self, collection, document):
        """
        The operation will create the collection if the collection does not currently exist.
        :param document: a dict to insert.
        """
        return self.db[collection].insert_one(document)


if __name__ == '__main__':
    import json
    helper = MongoHelper('test')
    helper.insert_document('testcollection', json.dumps({'a': 1, 'b.fe': 'qweq'}))
