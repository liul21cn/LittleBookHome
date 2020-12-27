# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/26
@Author      : Administrator
@File        : test_basics.py
@Description : 
"""

# test/test_basics.py
import unittest
from flask import current_app
from app import create_app,db

class BasicsTestCase(unittest.TestCase):
    """
    setup()和tearDown()方法分别在各测试前后运行，并且名字以test_
    开头的函数都作为测试执行
    """
    def setup(self):
        """
        在测试前创建一个测试环境：
        1）使用测试配置创建程序
        2）激活上下文，确保能在测试中使用current_app
        3）创建一个全新的数据库，以备不时之需
        """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        # 将app_context与当前环境结合
        self.app_context.push()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_app_exists(self):
        """
        测试当前app是否存在
        """
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        """
        测试当前app是否为测试环境
        """
        self.assertTrue(current_app.config['TESTING'])