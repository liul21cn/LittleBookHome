# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/20
@Author      : Administrator
@File        : __init__.py
@Description : 
"""

"""
1)创建蓝图
"""
from flask import Blueprint
# 实例化一个蓝图对象，指定蓝图的名字和蓝图所在的位置
auth=Blueprint('auth', __name__)

# 将路由与蓝本关联，一定要写在最后，防止循环导入
from . import views