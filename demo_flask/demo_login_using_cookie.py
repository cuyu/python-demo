#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 7/31/17
"""
from functools import wraps

from flask import Flask, request, Response, redirect
import time

app = Flask(__name__)


def check_cookie(func):
    @wraps(func)
    def wrapper():
        if not request.cookies:
            return redirect('/login')
        else:
            func()

    return wrapper


@app.route('/')
@check_cookie
def hello_world():
    return 'hello world'


@app.route('/login')
def login():
    res = Response('add cookies')
    res.set_cookie(key='name', value='foo', expires=time.time() + 60)
    return res


@app.route('/show')
@check_cookie
def show():
    return request.cookies.__str__()


@app.route('/del')
@check_cookie
def del_cookie():
    res = Response('delete cookies')
    res.set_cookie('name', '', expires=0)
    # print res.headers
    # print res.data
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
