#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 7/31/17
"""
from flask import Flask, request, Response, make_response
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/add')
def login():
    res = Response('add cookies')
    res.set_cookie(key='name', value='letian', expires=time.time() + 60)
    return res


@app.route('/show')
def show():
    return request.cookies.__str__()


@app.route('/del')
def del_cookie():
    res = Response('delete cookies')
    res.set_cookie('name', '', expires=0)
    # print res.headers
    # print res.data
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
