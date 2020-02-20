# -*- coding: utf-8 -*-
# @Time     :2020/2/1716:33
# @Author   :lei.qin
# @File     :runner.py
from testsuite.test_http import TestHttp
import unittest
from testsuite import test_http
from BeautifulReport import BeautifulReport
import os
import time
from tools.do_excel import Do_Excel
'''
方法一:逐条添加测试用例
# '''
# suite=unittest.TestSuite()
# suite.addTest(Test_lottery('test_not_find_lottery_kind'))
# suite.addTest(Test_lottery('test_lottery_history'))


'''
方法二:按测试类或模块添加
'''
#suite=unittest.TestSuite()
#loader = unittest.TestLoader() #创建一个加载器
#suite.addTest(loader.loadTestsFromTestCase(Test_lottery)) #添加该测试类下所有测试用例
#suite.addTest(loader.loadTestsFromModule(lottery_test_case)) #添加该模块下所有测试用例方法


now = time.strftime("%Y-%m-%d %H-%M-%S ",time.localtime(time.time()))
report_title = '用例报告'+ now + ".html"

report_path = os.getcwd() + '/report/'
desc = '老黄历接口测试'

if not os.path.exists(report_path):
    os.makedirs(report_path)
test_data = Do_Excel("test_data.xlsx", "oldyellowhistory").get_data()
suite = unittest.TestSuite()
for item in test_data:
    suite.addTest(TestHttp("api_test",item['url'],eval(item['data']),item['except1'],item['except2'],item['method']))
print(type(item),item)
runner = BeautifulReport(suite)
runner.report(description=desc,filename=report_title,report_dir=report_path)
# if __name__ == '__main__':
    # test_data = Do_Excel("test_data.xlsx", "oldyellowhistory").get_data()
    # suite = unittest.TestSuite()
    # suite.addTest(TestHttp("test_api",test_data[0]['url'],test_data[0]['data'],test_data[0]['except1'],test_data[0]['except2'],test_data[0]['method']))
    # runner = BeautifulReport(suite)
    # runner.report(description=desc,filename=report_title,report_dir=report_path)