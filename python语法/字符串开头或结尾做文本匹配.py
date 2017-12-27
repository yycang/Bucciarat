#############
# Cookbook2.2
#############


"""
场景: 需要在字符串开头或者结尾处按照指定的文本模式做检查, 例如检查文件的扩展民, URL协议等类型

解决方法: 1.用到字符串的方法str.startswith(), str.endswith()来解决; 2.切片; 3.正则
"""
import os
import re

filename = 'spam.txt'
res = filename.endswith('.txt')     # True
res1 = filename.startswith('file:')     # False

url = 'http://python.org'
res2 = url.startswith('http:')      # True

filename = os.listdir('.')      # os.listdir(path) 返回指定路径文件夹包含的文件以及文件夹名称的列表, 不包括'.'和'..'开头的文件

# 如果需要判断多个, 即给startswith或endswith提供包含可能选项的元组即可
res3 = any(name.endswith(('.py', '.txt')) for name in filename)   # True

# 传给startswith和endswith方法的参数必须是元组或者字符串, 如果遇到了列表和集合, 则使用tuple()将它们转换成元组


# 当然也能用切片来完成这个操作, 但是总感觉不太优雅
res4 = url[:5] == 'http:'       # True


# 正则同样可以来完成, 但是比较繁琐了
res5 = re.match('http:|https:|ftp:', url).group()   # http:



