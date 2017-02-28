#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 2/28/17
"""

from flask import Flask, Response

app = Flask(__name__)


@app.route("/normal_resource")
def hello():
    return "Hello World!"


@app.route("/cors_resource")
def cors_resource():
    resp = Response("Foo bar baz")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    # resp.headers['Access-Control-Allow-Methods'] = "GET, POST, PUT"
    return resp


if __name__ == "__main__":
    app.run()
