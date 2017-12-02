###########
# json是什么
###########

import json

"""

Json是一种轻量级的数据交换格式,使得人们很容易的进行阅读和编写,
同时也方便机器进行解析和生成,适用于数据交互的场景
格式为{"a": "123", "b": "456"}, 和python中数据类型字典一样~

"""


#############
# json转成字典
#############

data = '{"name": "cyy"}'
print(type(data))
dict_data = json.loads(data)    # 使用loads将json转成字典
print(type(dict_data))

data2 = json.dumps(dict_data)   # 使用dumps将字典格式转成json
print(type(data2))

f = open('temp.txt', 'w')
json.dump(dict_data, f)         # 将字典转成json类文件对象
f.close()

fr = open('temp.txt', 'r')
dict_data2 = json.load(fr)      # 将json类文件对象转成字典
print(dict_data2)
print(type(dict_data2))


"""

dumps: 将字典转成json字符串
loads: 将json字符串转成字典

dump:  将字典转成json的类文件对象
load:  将json的类文件对象转换成字典

类文件对象: 具有read()或者write()方法的对象
例如: f = open('a.txt', 'r')的f就是类文件对象

dumps和loads是在内存中进行转换
而涉及到类文件对象的dump和load则需在硬盘文件中进行转换, 但是很少用这种方式

"""