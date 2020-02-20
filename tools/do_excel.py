# -*- coding: utf-8 -*-
# @Time     :2020/2/17 18:47
# @Author   :lei.qin
# @File     :do_excel.py
from openpyxl import load_workbook


class Do_Excel():

    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def get_header(self):
        '''
            获取第一行标题行
        '''
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]
        header = []  # 存储标题行
        for j in range(1,sheet.max_column+1):
            header.append(sheet.cell(1,j).value)
        return header

    def get_data(self):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]
        header = self.get_header()  # 拿到header
        test_data = []

        for i in range(2,sheet.max_row+1):  # 1 2 3
            # i=1 j=1 2 3 4 5 6 7 8
            sub_data = {}
            for j in range(1, sheet.max_column+1):  # 1 2 3 4 5 6 7 8
                sub_data[header[j-1]] = sheet.cell(i, j).value
            test_data.append(sub_data)
            #print(test_data)
        return test_data


if __name__ == '__main__':
    print(Do_Excel("test_data.xlsx", "oldyellowhistory").get_data())
