# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/26
@Author      : Administrator
@File        : app.py
@Description : 
"""


from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


