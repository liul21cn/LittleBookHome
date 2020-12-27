# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : views.py
@Description : 
"""

"""
2) 应用蓝图
"""
from app.todo import todo

@todo.route('add')
def add():
    return 'todo add'

@todo.route('delete')
def delete():
    return 'todo delete'