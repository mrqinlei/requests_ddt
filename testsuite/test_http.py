# -*- coding: utf-8 -*-
# @Time     :2020/2/1715:45
# @Author   :lei.qin
# @File     :lottery_test_case.py
import unittest
from tools.http_request import HttpRequest
from ddt import ddt, data
import sys
from tools.do_excel import Do_Excel


test_data = Do_Excel("../tools/test_data.xlsx","oldyellowhistory").get_data()

@ddt
class TestHttp(unittest.TestCase):
    def setUp(self) -> None:

        print("开始执行")



    @data(*test_data)
    def test_api(self,item):
        res = HttpRequest().http_request(item['url'], eval(item['data']), item['http_method'])
        try:
            self.assertEqual(item['except1'], res['error_code'])
            self.assertEqual(item['except2'], res['reason'])
            print("响应内容{0}\n请求结果{1}\n请求错误码为{2}".format(res['result'],res['reason'],res['error_code']))
        except AssertionError as e:
            print("出错了{0}".format(e))
            raise e

    def tearDown(self) -> None:
        print("结束执行")
