# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : views.py
@Description : 
"""

"""
2）应用蓝图
"""
from app.auth import auth

@auth.route('/')
def index():
    return 'index'

@auth.route('/register')
def register():
    return 'register'

@auth.route('/login')
def login():
    return 'login'

@auth.route('/logout')
def logout():
    return 'logout'