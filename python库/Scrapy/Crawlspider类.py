"""

CrawlSpider类是定义了一些规则来提取link的比较方便进行获取请求的机制

本笔记内容包括:
1.CrawlSpider类的使用
2.Rule类
3.链接提取器

"""


######################
# 1.CrawlSpider类的使用
######################

"""

我们用命令创建普通的爬虫文件时是这样的:    scrapy genspider 爬虫名 域名

而创建CrawlSpider爬虫的时候只需要加上 -t crawl 即可
scrapy genspider -t crawl 爬虫名 域名

使用CrawlSpider类的区别原生scrapy框架的区别
1.导了两个包
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

分别是用作链接提取器和CrawlSpider类和Rule提取规则

2.本来爬虫中类继承于Spider类, 改成继承CrawlSpider

3.多了一个rules变量

4.没有了parse方法, CrawlSpider类中其实是有parse方法的, 但是没有在爬虫中写出来其实就是不让你重写parse方法

"""


##########
# 2.Rule类
##########

"""

主要使用rules来提取链接, rules是Rule对象的集合, 用来匹配目标网站并且排除不是该网站的网址

Rule类的参数:
linkextractor       从响应中提取链接
callback            处理链接的响应方法
follow              定义响应中提取的链接是否要跟进
process_links       对提取的链接进行过滤
process_requests    对生成的请求进行过滤

Rule对象的执行流程:

响应----(通过链接提取器写入规则提取指定的链接)----链接列表----(可以通过process_links参数对链接链表中进行操作)
----处理后的链接列表----(把链接生成请求,Request类)----请求----(process_requests把请求进行加工处理)
----处理后的请求----(发给引擎)----引擎(然后就是Scrapy那一套流程,由引擎交给调度器)

"""

############
# 3.链接提取器
############


"""

Link Extractor链接提取器

作用是从响应中提取链接

参数:
allow           满足该正则的链接将会被提取
deny            满足该正则的链接将不会被提取
allowed_domains 允许的域名
deny_domains    禁止的域名
restrict_xpaths 规定的xpath节点

链接提取器可以在CrawlSpider类中使用, 即使你继承了Spider类也可以使用, 因为它的作用很简单就是提取链接

CrawlSpider类可以通过链接提取器爬取整站, 爬取效率高


"""
