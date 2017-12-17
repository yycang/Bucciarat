"""

MySQL官方网站:  https://www.mysql.com/

本笔记涉及内容有:
1.MySQL安装与启动
2.数据的完整性
3.数据库操作
4.数据表操作
5.数据简单的增删改查操作

"""

#################
# 1.MySQL安装与启动
#################

"""

服务器端安装:     sudo apt-get install mysql-server
客户端安装:      sudo apt-get install mysql-client

启动服务:       sudo service mysql start
停止服务:       sudo service mysql stop
重启服务:       sudo service mysql restart

连接数据库:      mysql -uroot -pmysql

"""

##############
# 2.数据的完整性
##############

"""

为了使数据更具备完整性和有效性, 在创建表的过程中, 对表的数据添加一些强制性的验证, 例如数据的类型和约束

常用数据类型:
整数:         int
小数:         decimal(4,2)     (浮点型, 一共有4位, 小数占2位)
字符串:        varchar, char    char固定长度的字符串, 如char(4), 存储'aa'时会强行填充两个空格, 而varchar这种可变长度字符串就比较灵活了
日期时间:      data, time, datatime
大文本:        text    字符大于4000时候使用的大文本
枚举:         enum('1', '2', '3')

详细:
TINYINT:    字节大小1   范围0~255     存储年龄
DATA:       字节大小4   示例: '2020-01-01'
TIME:       字节大小3   示例: '12:29:59'
DATETIME:   字节大小8   示例: '2020-01-02 12:29:59'

约束:
主键:     primary key 保证数据的唯一性
非空:     not null    不能为空值
唯一:     unique      字段值不允许重复
默认:     default     如果不填写此值时会填写默认值
外键:     foreign key 对关系字段进行约束, 当关系字段填写值时会到关联的表中查询此值是否存在

"""

############
# 3.数据库操作
############

"""

查询当前服务端的时间:     select now();

查看数据库:             show databases;

修改输入提示符:          prompt cyy>;

使用数据库:             use <数据名>;

查看当前使用的数据库:     select database();

创建数据库:             create databases <数据库名> charset=utf8;(指定编码集为utf8)

查看创建的数据库信息:     show create database <数据库名>;

删除数据库:             drop database <数据库名>;

"""

############
# 4.数据表操作
############

"""

查看当前数据库的所有表:   show tables;

查看表的创建信息:        show create table <表名>;

查看表的结构:           desc <表名>;

创建数据表:             create table <表名> (
                      id int unsigned primary key not null auto_increment,
                      name varchar(10),
                      age tinyint unsigned,
                      height decimal(5,2),
                      gender enum('男','女','人妖','保密')
                    );
**:auto_increment 实现自增长, unsigned 为无符号类型

删除表:                drop table <表名>

修改表结构:
添加字段add               alter table <表名> add money(新字段) int not null(字段类型);
修改字段change            alter table <表名> change money(原字段) houses(新字段) varchar(50) not null(新字段类型);
修改类型modify            alter table <表名> modify house varchar(50);
删除字段drop              alter table <表名> drop house;

"""

######################
# 5.数据简单的增删改查操作
######################

"""

增
insert into <表名> values (0, '沧源远', 18, 180.00, 1);
对应表结构进行添加, id已经实现自增长, 可以用0,null等占位即可, 上述为全列插入, 一条都不可少

insert into <表名> (name, age, gender) values ('石原里美', 18, 2);
指定列插入, 指定字段进行插入, 未设置为null

insert into <表名> (name, age, gender) values ('石原里美', 18, 2), ('新垣结衣', 17, 2), ('toda', 16, 2);
批量插入

删
delete from <表名> where id = 2;
虽然where id = 2可以省略, 但是省略之后就是将表里的数据全部删除, 慎重, 慎重

改
update <表名> set name='路飞', age=18;
批量修改, 全部名字修改为路飞, 全部年龄修改为18, 同样慎重, 慎重

update <表名> set name='索隆' where id=3;
指定修改

查
select * from <表名>;
查询所有, 也可以用where来指定查询

"""