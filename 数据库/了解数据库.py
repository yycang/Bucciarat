"""

数据库排名:  https://db-engines.com/en/ranking

本笔记涉及内容有:
1.RDBMS
2.SQL
3.MySQL

"""


#########
# 1.RDBMS
#########

"""

RDBMS
Relational Database Management System
关系型数据库管理系统

对一个类型的数据库的统称(oracle, sql server, MySQL)

oracle: 收费, 并且很贵, 在大型项目中使用, 银行, 电信等项目
mysql: 免费, 最广泛
sql server: 微软项目使用

以上数据库都是要和服务端进行交互来拿取数据
下面这个数据库是单机版

sqlite: 轻量级数据库, 应用在app中

核心元素:

数据行, 数据列, 数据表, 数据库

抽象化一点来看:
行相当于Python中的实例对象
那么列就相当于对象的实例属性
表就相当于存储列表
库就相当于存储集合, 一个数据库里可以有n个数据表

"""

#######
# 2.SQL
#######

"""

SQL
Structured Query Language
结构化查询语言

可以通过SQL查询一切关系型数据库

sql语句主要分为:
DQL:    数据查询语言, select
DML:    数据操作语言, 增删改, insert, delete, update
TPL:    事物处理语言, commit, rollback
DCL:    数据控制语言, 进行授权与权限回收, grant, revoke
DDL:    数据定义语言, 进行数据库,表的管理, create, drop
CCL:    指针控制语言, 通过控制指针完成表的操作, declare cursor

虽然不区分大小写, 但是广泛的书写风格是关键字大写, 绝大多数命令用一个分号来结束一条SQL语句

"""

#########
# 3.MySQL
#########

"""

由瑞典MySQL AB公司开发, 后来被Sun公司收购, 最后被Oracle公司收购
现在隶属于Oracle旗下

最主要的特点:
开源, 免费, 使用范围广, 跨平台支持性好, 提供了多语言调用的API

"""
