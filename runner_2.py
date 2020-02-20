# -*- coding: utf-8 -*-
# @Time     :2020/2/18 17:21
# @Author   :lei.qin
# @File     :runner_2.py
import unittest
from testsuite.test_http import TestHttp
import unittest
from testsuite import test_http
from BeautifulReport import BeautifulReport
import os
import time
from tools.do_excel_2 import DoExcel

now = time.strftime("%Y-%m-%d %H-%M-%S ",time.localtime(time.time()))
report_title = '用例报告'+ now + ".html"

report_path = os.getcwd() + '/report/'
desc = '老黄历接口测试'

t= DoExcel("test_data.xlsx", "oldyellowhistory")
suite=unittest.TestSuite()
for i in range(1,t.max_row+1):
    suite.addTest(TestHttp("api_test",t.get_data(i,1),eval(t.get_data(i,2)),t.get_data(i,3),t.get_data(i,4),t.get_data(i,5)))
runner = BeautifulReport(suite)
runner.report(description=desc,filename=report_title,report_dir=report_path)