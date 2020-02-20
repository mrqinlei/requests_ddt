# -*- coding: utf-8 -*-
# @Time     :2020/2/1715:45
# @Author   :lei.qin
# @File     :lottery_test_case.py
import unittest
from tools.http_request import HttpRequest


class TestHttp(unittest.TestCase):
    def setUp(self) -> None:

        print("开始执行")

    def __init__(self,methodName,url,data,except1,except2,method):
        super(TestHttp,self).__init__(methodName)
        self.url = url
        self.data = data
        self.method = method
        self.except1 = except1
        self.except2 = except2



    def api_test(self):
        res = HttpRequest().http_request(self.url, self.data,self.method)
        try:
            self.assertEqual(self.except1, res['error_code'])
            self.assertEqual(self.except2, res['reason'])
        except AssertionError as e:
            print("出错了{0}".format(e))
            raise e



    def tearDown(self) -> None:
        print("结束执行")
