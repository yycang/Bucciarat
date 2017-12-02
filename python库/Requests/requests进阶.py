"""

requests中文文档: http://docs.python-requests.org/zh_CN/latest/

源码地址: https://github.com/requests/requests

本笔记涉及requests进阶内容:
1.处理session和cookie
2.cookie对象转换成字典
3.SSL证书验证
4.设置超时

"""

import requests

#######################
# 1.处理session和cookie
#######################

# 这次用面向对象来做笔记


class Set_cookie(object):
    def __init__(self):
        self.url = 'https://www.zhihu.com'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
            "Cookie": 'zap=685ab010-66bd-442b-a9e5-8bc66dec783e; d_c0="AGDCo7BAnwyPTuZkKfHCnAdxNydRGcA3zDA=|1509625697"; aliyungf_tc=AQAAADHqVnRvdQIAK3CCDk+psfULMevd; q_c1=89522ece92ac48d891f5a07adbdb5ee1|1512116145000|1509450192000; l_cap_id="ZDFkMDYxMmM2NTVhNDU3OWIyNjJjYjk0ODFjZGM3N2U=|1512129420|a5d6cd89ce27d512305d61812c1403ddc0b9e57b"; r_cap_id="M2U4ZjYwZDAwMTE5NDQwYjk0MjFmOTkwYTA1YjU4N2I=|1512129420|b42c0d567455aed199a1237b52919ab85ebcf737"; cap_id="ZjQ3NzM5Njc0ZjY3NGYwOThlOWMyZjU2M2RjYzYxNmI=|1512129420|27799783b8149eb1a785d86a052e28f1caf486c7"; capsion_ticket="2|1:0|10:1512130773|14:capsion_ticket|44:YzAwZTk2NzNjYjYxNDk2YmI0MjhhM2NkMTA5NGE1OTk=|be6a62466673e2a2d7c250d5fce2ac00f33c065fc4684b4fcae72764abee4414"'
        }       # 第一种方法Cookie是以字典的格式放在请求头中携带过去(上面的Cookie是随便粘贴过来的,并不能用,示例而已)

        self.headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        }
        self.temp = "anonymid=j6c96snx6i82ml; _r01_=1; depovince=BJ; JSESSIONID=abcuKWLdqxTjJbjrR9X7v; jebe_key=2b511d4c-0b0e-4e77-bcbd-28616d344a3d%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1507298042637%7C1%7C1507298042328; _ga=GA1.2.1361939841.1504226199; _gid=GA1.2.1639587085.1507300736; ch_id=10016; jebecookies=01f29853-5d04-48d0-a2d4-0ef2bfa1657e|||||; ick_login=044f4772-831d-4a9d-9f7d-29b6051ee4b6; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=c3148efff984658f83e0ccb5b36598b75; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1f694eb301b54924d148c04eca6da9b35; societyguester=1f694eb301b54924d148c04eca6da9b35; id=923768535; xnsid=b77fd1e; ver=7.0; loginfrom=null; wp_fold=0"

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode()

    def manage_data(self):
        """
        这里将Cookie的值用;切割,从而组成相应的键值对(=左边为key,=右边为value),返回一个字典
        :return:
        """
        temp_dict = {}
        for data in self.temp.split('; '):
            temp_dict[data.split('=')[0]] = data.split('=')[1]
        return temp_dict

    def get_data2(self, temp_dict):
        response = requests.get(self.url, headers=self.headers2, cookies=temp_dict)
        # 第二种方法是使用cookie参数, 传递一个字典
        return response.content.decode()

    def run(self):
        data = self.get_data()
        temp_dict = self.manage_data()
        data2 = self.get_data2(temp_dict)
        # 这两种方法得到的页面都是登录后的界面
        print(data, data2)

"""

cookies传递:
1.请求头中添加
2.使用cookie参数

"""


class set_session(object):
    def __init__(self):
        self.url = 'http://www.renren.com/PLogin.do'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
        }
        self.post_data = {
            "email": "xxxxxxxxxx",
            "password": "xxxxxxxxxx"
        }           # 这里是构建表单数据,简单的模拟登录

    def get_data(self):
        # 创建一个session实例
        session = requests.session()
        # 使用session发送请求
        session.post(self.url, headers=self.headers, data=self.post_data)

        # get请求
        response = session.get('http://www.renren.com/xxxxxxxx')

        # 实现模拟登录之后,就不用担心cookie了,session会帮我们保存会话
        return response.content.decode()

    def run(self):
        data = self.get_data()
        print(data)


"""

requests提供了一个session的类, 来提供会话保持:
1.实例化一个对象
session = requests.session()
2.使用对象发送请求
session.get(url)
session.post(url, data=data)

"""

####################
# cookie对象转换成字典
####################

url = 'http://www.baidu.com'
response = requests.get(url)
print(response.cookies)         # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
print(type(response.cookies))   # <class 'requests.cookies.RequestsCookieJar'>

dict_data = requests.utils.dict_from_cookiejar(response.cookies)
jar_data = requests.utils.cookiejar_from_dict(dict_data)

"""

cookie的返回对象为RequestsCookieJar
可以用utils里面的小方法完成它们之间的相互转换

requests.utils.dict_from_cookiejar  把cookie对象转化为字典
requests.utils.cookiejar_from_dict  把字典转化成cookie对象

"""


############
# SSL证书验证
############

url = 'https://www.12306.cn/mormhweb/'

response = requests.get(url, verify=False)

"""

Requests可以为HTTPS请求验证SSL证书,默认是开启的,如果SSL证书验证失败会抛出一个异常SSLError
Requests可以忽视对SSL证书的验证,通过将verify设置成Fasle
忽视验证之后会提示相关的警告信息,但是依然可以获取html源码

"""


#########
# 设置超时
#########

url = 'https://www.youtube.com'

requests.get(url, timeout=3)

"""

timeout参数可以为请求增加一个时间,单位为秒
如果超过该时间就不会再请求下去
可以用作多线程多进程爬虫,或者验证代理ip的有效性

"""
