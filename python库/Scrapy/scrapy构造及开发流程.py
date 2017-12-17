"""

scrapy框架官方文档 1.4:   https://doc.scrapy.org/en/latest/

scrapy框架中文文档 1.0:   http://scrapy-chs.readthedocs.io/zh_CN/1.0/index.html

源码地址:                https://github.com/scrapy/scrapy

本笔记涉及内容有:
1.框架结构与各模块功能
2.scrapy框架的使用流程
3.scrapy shell
4.Spider类
5.Request类
6.反反爬中间件
7.log信息

"""

import scrapy

#####################
# 1.框架结构与各模块功能
#####################

"""

为什么要用Scrapy框架, Scrapy的优点:
1.提供了整套项目的打包方案, 开发速度快
2.使用scrapy框架开发的项目, 稳定性高
3.scrapy框架的底层实现非常优秀, 性能优越
4.使用scrapy框架实现分布式爬虫简单

Scrapy组件功能解析:

引擎:     处理整个系统各个模块之间的数据流
下载器:    接受请求, 返回响应
调度器:    接收请求, 压入队列  引擎再次请求时返回请求
爬虫:     发起起始的请求, 定义爬取页面的方法
item管道: 处理后续数据

下载器中间件:     处理引擎与下载器之间的请求及响应(反反爬)

爬虫中间件:      处理spider的响应输入和请求输出

流程:
1.从爬虫模块发起最初的url请求, 通过引擎传到了调度器(引擎是所有模块的枢纽, 所有模块交互都要经过它)
2.调度器接到了爬虫模块发起的请求后, 加入队列, 然后等引擎来拿时返回请求(不仅仅是放进去再拿出来, 肯定会有高级操作的嘛)
3.下载器接受到调度器的请求后, 解析返回响应(相当于requests.get(url)这句话)
4.引擎再把下载器中得到的响应传给爬虫, 爬虫通过爬取页面的方法, 将数据通过引擎传给item管道(同时可以从数据中提取url再次跳到1的步骤)
5.item管道处理后续数据

"""


####################
# 2.scrapy框架使用流程
####################

"""

构建一个scrapy项目的流程很简单, 就四步

普通的爬虫流程:    分析站点---提交url请求获取响应---从响应中解析数据和获取新的url---处理数据---保存数据

scrapy的流程:
1.创建项目      scrapy startproject <项目名>
(当创建完成后, 会给出相应的提示: 让你cd进项目目录, 并且可以用scrapy genspider example 'example' 来创建你的爬虫文件)

创建后的项目目录:
tutorial/
    scrapy.cfg            # 部署配置文件用的(不是部署超级瞄准的哦)

    tutorial/             # 项目模块文件, 主要写代码的地方
        __init__.py       # 当包用

        items.py          # item建模

        middlewares.py    # 中间件(反反爬)

        pipelines.py      # 处理后续数据(比如存储数据)

        settings.py       # 设置文件

        spiders/          # 爬虫文件存放目录(里面的爬虫文件可以手动创建, 也可以用刚才提到的方法创建)
            __init__.py

2.明确目标
根据你的要爬的目标在item中创建模型, 比如你想要爬取名称,url,作者,阅读量,文章等数据
很简单的使用 name = scrapy.Field()    url = scarpy.Field()    等等就可以完成建模了(字段类型统一为Field)
用这个模板创建的实例具备字典的方法, 可以当成字典来用, 但是比字典厉害在于可以检查字段名(存在错误会报错)
"""
# 例子:


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

"""
3.创建爬虫
刚刚提到了有两种方法
(1)命令创建     scrapy genspider 生成的爬虫名 '允许的域名'
(爬虫名不能和项目名重名, 且具备唯一性)
(2)手动创建     在spiders目录下创建爬虫文件
必要参数:   name    allowed_domains     start_urls      parse方法  (三个参数,一个方法,命名固定)

运行爬虫    scrapy crawl 爬虫名
"""

# 例子:


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):           # response自带xpath方法
            title = sel.xpath('a/text()').extract()     # extract()转成unicode字符串
            link = sel.xpath('a/@href').extract()       # extract()返回一个列表
            desc = sel.xpath('text()').extract()        # extract_first()返回列表第一个元素
            print(title, link, desc)


"""
4.保存内容
最简单的储存爬取数据的方法:  Feed输出, 返回一个unicode文件
命令:
scrapy crawl dmoz -o items.json

还可以编写pipelines管道文件进行存储数据
process_item    用来定义对数据的操作, 必须返回item
open_spider和close_spider    用来处理爬虫运行时和结束时的处理, 可以用来打开和关闭文件
编写完管道文件记得在设置中开启

"""


################
# 3.scrapy shell
################

"""

scrapy shell
浏览器显示的页面是通过加载, 解析, 渲染之后的结果, 而且scrapy不能处理动态加载页面
所以可以用scrapy shell <url> 对网站发起一次请求, 方便进行调试

可以用shelp来查看shell的帮助命令

response.url    查看请求的url

response.text   查看字符串源码

response.body   查看源码(二进制类型)

response.headers    查看响应头

response.status     查看状态码

response.xpath()    查看xpath

response.css()      查看css

加载用户头启动:    scrapy shell -s USER_AGENT=''

获取新的requests:    fetch(url)

用本地浏览器打开给定的response, 创建一个临时文件, 且不会被删除

"""


############
# 4.Spider类
############

"""

Spider类定义了爬取哪些网站, 怎样爬取数据和爬取哪些items等方法

scrapy.Spider
最基本的类，所有编写的爬虫必须继承这个类

name    定义spider名字, 必须项, 唯一项(可以生成多个相同的spider实例)

allowed_domains     可选, 包含spider允许爬取的域名列表

start_urls      url列表, 当没有指定的url可以提取的时候, 爬虫从这个列表中开始爬, 通常爬取的第一个url就在此列表中

start_requests()    该方法必须返回一个可迭代对象(iterable)。该对象包含了spider用于爬取的第一个Request
该方法使用start_urls里面的url生成Request

make_requests_from_url(url)     旧方法, 效果同start_requests()方法, 使用时会发出警告让你用新方法

parse(response)     负责处理response并返回处理的数据和跟进的url


"""


#############
# 5.Request类
#############

"""

Request通常是对url发起get请求, 获取响应
参数:
    url         目标url
    callback    目标url响应的解析函数
    meta        传参(应用于列表页的item传到详情页中)
    headers     请求头
    dont_filter 该请求是否会被调度器过滤(默认为False即会被过滤)
    cookies     cookies参数

而发送Post请求有两个方法:
FormRequest类继承自Request类
参数继承Request,
formdata        表单参数(字典格式)

例子:
return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name': 'John Doe', 'age': '27'},
                    callback=self.after_post)]

同时发送post请求还有另外一种方法:     FormRequest.from_response
参数:
    response
    formdata
    callback
特性在于可以自动获取表单并将表单数据提交

"""
# 例子, 实现模拟登录


class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return


##############
# 6.反反爬中间件
##############


"""

爬虫会占用服务器的资源, 影响正常用户, 所以服务器必须要做反爬
同时也为了保护自己公司的数据不被爬取

服务器常见的反爬手段:
判明用户身份      用户头, Cookies, 验证码等
分析用户行为      在线活动时间, 并发识别, 添加正常浏览器不能访问
动态加载数据      ajax, js

反反爬措施:
1.模拟用户头
在setting中设置, 或在下载器中间件设置动态用户头
2.请求延迟
setting文件中 DOWNLOAD_DELAY = n(默认是3s, 每3s发送一个请求)
3.Cookie检测
setting文件中COOKIES_ENABLED = False
4.IP代理池
5.动态数据加载
使用selenium

使用中间件的时候, 需要在setting中进行设置

"""


##########
# 7.log信息
##########

"""

当你输出爬虫时会产生很多log信息, 如果这些信息很碍事的话, 可以选择关闭它们

LOG_ENABLED     是否开启log

当然还有其他方法, 比如把log信息写入到文件中

LOG_FILE = '文件.log'

当然你想筛选出log信息也是可以的, log信息分为5个等级

LOG_LEVEL = ' '
            CRITICAL    严重错误
            ERROR       一般错误
            WARNING     警告信息
            INFO        一般信息
            DEBUG       调试信息
    (如果你设置了一个等级, 那么这个等级上面的信息也会被自动打印出来, 例如设置为INFO, 那么除了DEBUG调试信息不会显示, 其他信息也会显示)


部署时候可能会用到的参数:
CONCURRENT_REQUESTS     下载器并发数量设置, 默认16
DEPTH_LIMIT             爬取深度
DOWNLOAD_TIMEOUT        设置超时时间
CONCURRENT_ITEMS        item管道同时处理item数量
CONCURRENT_REQUESTS_PER_DOMAIN      域名的并发请求
CONCURRENT_REQUESTS_PER_IP          ip的并发请求数量

"""