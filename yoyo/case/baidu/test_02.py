# coding:utf-8
import unittest
from selenium import webdriver

class Test1(unittest.TestCase):
    u'''用例自己写'''
    def setUp(self):
        print("start!")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(30)

    def tearDown(self):
        print("end!")
        self.driver.close()

    def test_01(self):
        u'''测试百度搜索：yoyo'''
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        print("测试百度的案例")


    def test_02(self):
        u'''测试百度搜索：haha'''
        self.driver.find_element_by_id("kw").send_keys("haha")

if __name__ == "__main__":
    unittest.main()
