"""

MongoDB官网:  https://www.mongodb.com/

本笔记涉及内容:
1.启动MongoDB
2.数据库操作
3.集合的操作
4.数据类型
5.增删改查

"""


##############
# 1.启动MongoDB
##############

"""

服务端的命令是mongod

mongod --help       查看所有参数
(配置文件在/etc/mongod.conf, 默认端口号为27017)

启动
sudo service mongod start

停止
sudo service mongod stop

重启
sudo service mongod restart

客户端的命令是mongo
直接进入shell程序

"""

#############
# 2.数据库操作
#############

"""

查看当前数据库         db

查看所有数据库         show dbs  (显示物理上存在的数据库, 即如果这个数据库没有任何集合, 则该数据库不会被物理的创建)

切换数据库            use <数据库名>

删除数据库            db.dropDatabase()  (删除当前使用的数据库)

"""

############
# 3.集合的操作
############

"""

创建集合            db.createCollection(<集合名>, options)
options可以添加参数{'capped': true, size: 10},
capped默认为False不设置上限, size为如果capped为true需要指定上限大小, 文档达到上限会将之前的数据覆盖(先进数据先淘汰)
如果设置的默认大小小于256字节, 都会默认等于256字节

查看集合            show collections

删除集合            db.<集合名>.drop()

"""

###########
# 4.数据类型
###########

"""

Object ID:          文档ID
String:             字符串
Boolean:            存储一个布尔值
Integer:            整数, 32位或者64位
Double:             存储浮点值
Arrays:             数组或列表
Object:             嵌入式文档, 一个值为一个文档
Null:               存储Null值
Timestamp:          时间戳
Date:               存储当前日期时间

object id 是每个文档都会拥有的一个属性, 为_id, 保证每个文档的唯一性
可以自己设置
_id构成:
前四位为时间戳
接下来三个字节为机器的id
接下来两个字节为MongoDB服务进程id
后三个字节为增量值

"""

###########
# 5.增删改查
###########

"""

增
db.<集合名>.insert(document)
例如: db.<集合名>.insert({name: 'cyy'})

删
db.<集合名>.remove({query}, {justOne: boolean})
参数justOne设置后为只删除满足数据的第一条数据
db.<集合名>.remove({name:'cyy'}, {justOne: true})
db.<集合名>.remove({}) 删除所有的数据

改
db.<集合名>.update({query}, {update}, {multi: boolean})
第一个参数选择要更新的条件, update表示更新后的, 最后这个参数默认为False, 即只更新匹配到的第一条数据, 设置为true后表示把满足条件的所有数据全部更新
db.<集合名>.update({age:18},{name:'yyc'}) 这样的更新方式会将查询到age为18的第一条数据更新成name:'yyc', 也就意味着更改了文档的结构
db.<集合名>.update({age:18},{$set:{name:'yyc'}}) $set表示指定字段更新

查
db.<集合名>.find()

保存
db.<集合名>.save(document)
如果_id已经存在则更新, 不存在则添加

"""