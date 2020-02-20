# -*- coding: utf-8 -*-
# @Time     :2020/2/1713:47
# @Author   :lei.qin
# @File     :http_request.py
import requests
class HttpRequest:
    '''
    利用requests封装get请求和post请求
    '''
    def http_request(self,url,data,method,cookie=None):
        ''' url:请求地址
            param:传递的参数 非必填参数 字典格式
            method:请求方法
            cookie:请求的时候传递的参数值
        '''
        if method.lower() == "get":
            res = requests.get(url, data, cookies=cookie)  # 响应结果的消息实体
        elif method.lower() == "post":
            res = requests.post(url,data,cookies=cookie)#响应结果的消息实体
        return res.json() #返回消息实体
if __name__ == '__main__':
    search_url = "http://apis.juhe.cn/lottery/query"
    search_data = {"key": "4f8fbb9a8a29d861b84303292cb19f85","lottery_id":31231212}
    res = HttpRequest()
    r = res.http_request(search_url,search_data,"post")
    print(type(r))
    print(r)