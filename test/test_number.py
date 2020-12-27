# -*- coding: utf-8 -*-

"""
@Time        : 2020/12/26
@Author      : Administrator
@File        : test_number.py
@Description : 
"""

# test/test_number.py
import unittest
from random import random


class TestSequenceFunctions(unittest.TestCase):
    """
    setup()和tearDown()方法分别在各测试前后运行，并且名字以test_开头
    的函数都作为测试执行
    """
    def setUp(self) -> None:
        self.seq = [0, 1, 2, 3, 4, 5, 6, 7]

    def test_choice_ok(self):
        item = random.choice(self.seq)
        result = item in self.seq
        self.assertTrue(result)

    def test_sample_ok(self):
        result = random.sample(self.seq, 4)
        self.assertEqual(len(result), 4)

    def tearDown(self) -> None:
        del self.seq