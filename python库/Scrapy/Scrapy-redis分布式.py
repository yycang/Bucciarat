"""

源码地址: https://github.com/rmax/scrapy-redis

本笔记包含:
1.Scrapy-redis配置
2.Scrapy-redis分布式组件
3.改造为分布式爬虫
4.持久化存储


"""


###################
# 1.Scrapy-redis配置
###################

"""

windows下, 进行Redis安装步骤

1.下载程序并解压
2.修改配置文件, 如果链接服务器为本地, 注释掉
3.配置环境变量, 管理员方式启动cmd并输入 redis-server即可开启

Linux下

1. sudo vi /etc/redis/redis.conf    注释本地连接, 允许远程链接
2. sudo redis-server /etc/redis/redis.conf  启动

链接:

主机端:    redis-cli
非主机端:   redis-cli -h master_ip

链接后开启分布式爬虫:
运行分布式爬虫文件   scrapy runspider ****.py
将起始的url和key扔进队列中:

lpush key(文件中设置) 起始的url

"""


########################
# 2.Scrapy-redis分布式组件
########################

"""

由多台机器来完成一个任务, 从而缩短任务的执行时间

优点在于:   提升速度,   单个节点不稳定不会影响整个任务的执行

分布式组件结合了redis数据库和scrapy框架, 弥补了scrapy框架不能做分布式的缺点

scrapy和scrapy-redis组件区别

                    scrapy                  scrapy-redis
scheduler(调度器):  请求在调度器中执行          将数据放到redis数据库队列中处理
Duplication Filter
(重复过滤器):        请求指纹,用python集合      在redis数据库的set中去重
itempipeline:      决定数据如何处理的中间件     将数据存放到redis数据库队列中
Spider:            普通的scrapy爬虫类         可以从redis中获取url

"""

#################
# 3.改造为分布式爬虫
#################

"""

步骤:
1.导入分布式爬虫类
from scrapy_redis.spiders import RedisSpider

2.修改爬虫的继承
class XXXX(RedisSpider)

3.注销allowed_domains和start_urls

4.动态获取允许的域
def __init__(self, *args, **kwargs):
    domain = kwargs.pop('domain', '')
    self.allowed_domains = list(filter(None, domain.split(',')))
    super(XXXX, self).__init__(*args, **kwargs)

5.添加redis_key
redis_key = '随意写值'

6.修改配置文件

(1)# 指定调度器中的重复过滤器使用scrapy_redis的重复过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
(2)# 指定调度器为scapy_redis中的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
(3)# 调度器是否保持任务队列, 开启支持断点续传
SCHEDULER_PERSIST = True

# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"   # 优先队列, 默认
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"           # 普通队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"           # 栈

(4)ITEM_PIPELINES = {
    # 'XXXX.pipelines.ExamplePipeline': 300,
    # 负责将数据传输到redis数据库中数据队列
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
(5)# 链接数据库
REDIS_URL = "redis://172.16.123.128:6379"


"""

############
# 4.持久化储存
############

"""

将redis中存储的item数据存储到其他数据库中

原因: redis内存数据库, 容量有限, 并且容易丢失数据, 一般存储数据都用MongoDB或者SQL

存入MongoDB中的demo:

"""

import redis
from pymongo import MongoClient
import json

# 链接redis数据库
redis_cli = redis.Redis(host='主机ip', port=6379, db=0)
# 链接mongo
mongo_cli = MongoClient('127.0.0.1', 27017)
db = mongo_cli['xxx']
col = db['xx']

while 1:
    # 从redis中读取数据
    source, data = redis_cli.blpop(['xxx:items'])  # 返回一个元组, 前者为键, 后者为数据
    # 我们想要的数据存在data中, 转成字典存入mongodb
    dict_data = json.loads(data)
    col.insert(dict_data)