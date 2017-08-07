# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    u'''随便写的几个'''
    def setUp(self):
        print("start!")
    def tearDown(self):
        time.sleep(1)
        print("end!")
    def test01(self):
        print("执行测试用例01")

    def test03(self):
        print("执行测试用例03")

    def test02(self):
        print("执行测试用例02")
if __name__ == "__main__":
    unittest.main()