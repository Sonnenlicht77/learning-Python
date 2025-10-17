"""
一个类型六个方法
一个类型：一个数据类型 HTTPResonpse
六个方法： read readline readlines getcode geturl getheaders
"""

import urllib.request

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url)

# 一个类型 HTTPResponse
typeResponse = type(response)
print(typeResponse) # <class 'http.client.HTTPResponse'>

# 六个方法
"""
    read(): 读取整个页面,按字节返回
    readline(): 读取一行
    readlines(): 读取所有行
    getcode()： 返回响应体的状态码
    geturl(): 获取当前请求的地址url
    getheaders() :获取请求头信息
"""
# content = response.read().decode('utf-8')
# content = response.readline() # b'<!DOCTYPE html>\n'
# content = response.readlines() # 读取所有行
# print(content)

# 获取状态码
statusCode = response.getcode()
print(statusCode) # 200 状态码

# 获取当前请求的地址url
geturl = response.geturl()
print(geturl) # http://www.baidu.com

# 获取请求头
get_headers = response.getheaders()
print(get_headers)




