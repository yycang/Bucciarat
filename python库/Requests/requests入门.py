"""

requests中文文档: http://docs.python-requests.org/zh_CN/latest/

源码地址: https://github.com/requests/requests

本笔记涉及requests基础内容:
1:发送请求
2:获取响应信息
3:简单伪装:加上请求头
4:携带参数
5:发送post请求
6.使用代理

"""
import requests

###########
# 1.发送请求
###########

r = requests.get('https://www.baidu.com')    # 注意传递的url必须携带协议

# 同时还能使用post, put, delete, head, options等一系列的http请求方式

# 返回一个名字为r的response对象, 在这个对象中可以获取我们想要的信息


##############
# 2.获取响应信息
##############

"""

response对象的常用方法:
response.text               获取str类型的响应
response.content            获取bytes类型的响应
response.status_code        获取状态码
response.request.headers    获取请求头
response.headers            获取响应头
response.url                获取响应的url, 包括追加了url参数之后完整的url, 或者重定向之后的url, 有可能会和传入的url不一样

"""

print(r.encoding)           # ISO-8859-1 (Requests推测出来的文本编码, 会显示乱码)

print(r.text)               # <!DOCTYPE html><!--STATUS OK--><html> <head><meta...

print(r.content)            # b'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta...

print(r.status_code)        # 200

print(r.request.headers)    # {'User-Agent': 'python-requests/2.9.1', 'Connection':...

print(r.headers)            # {'Date': 'Thu, 30 Nov 2017 12:56:57 GMT', 'Last-Modified':...

print(r.url)                # http://www.baidu.com/

"""

r.text和r.content

.text类型是str字符串格式, 如果出现乱码可以通过修改encoding属性来改变他

r.encoding = 'utf-8'

.content类型是bytes二进制格式, 如果要转成字符串类型用decode方法即可

r.content.decode()

"""


############
# 3.加入请求头
############

url = 'https://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
}         # headers的字典格式

response = requests.get(url, headers=headers)

# 伪装请求头让我们的爬虫更像浏览器从而获取和浏览器访问一样的内容


##########
# 4.携带参数
##########

url = 'https://www.baidu.com/s?'     # 分析出百度搜索传递参数格式为 https://www.baidu.com/s?wd=小姐姐

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
}

params = {
    'wd': '小姐姐'
}       # 参数的形式也为字典格式

response2 = requests.get(url, headers=headers, params=params)


###############
# 5.发送post请求
###############

data = {
    'key1': 'value1',
    'key2': 'value2'
}       # post请求传输的数据也是data格式

response3 = requests.post(url, headers=headers, data=data)  # 这里发送post请求,十分简单


#############
# 6.使用代理
#############

"""

两个获取免费代理ip的网站:
http://www.kuaidaili.com/free
http://www.data5u.com/free/index.shtml

"""

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}

response4 = requests.get(url, headers=headers, proxies=proxies)

