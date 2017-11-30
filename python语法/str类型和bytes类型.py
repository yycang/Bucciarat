##################
# str类型和bytes类型
##################

"""

bytes: 二进制类型  (存在于python3中)
互联网上的数据都是以二进制的方式传输

str: unicode的呈现形式

ASCII码(美国信息互换标准代码): 最初的字符集, 仅保存英文文字
GB2312, GB18030字符集:  为了让计算机能读懂中国的汉字, 中国聪慧的程序员将原来的字符集不停扩展, 增加了许多中文汉字
这时各个国家都像中国一样弄出了一套关于他们自己语言的编码标准, 放在计算机上一瞧, 谁也不认识谁, 各个编码互不支持
UNICODE字符集:  于是诞生了这套全世界语言统一的字符集编码

ASCII是一个字节,而UNICODE通常是两个字节
这样在保存英文文本时会造成浪费了一倍的空间资源!
UTF-8:  是一种编码格式, 关键在于他的可变长性, 可以是1, 2, 3个字节, 如果要用一个字节存一个字符就用一个, 如果要用两个字节存一个字符就用两个
这样就可以充分利用到空间而不会造成浪费

"""

####################
# str和bytes之间的转换
####################

data = '沧源远'
print(type(data))   # str类型
print(data)         # 沧源远

print('-' * 30)
b_data = data.encode()
print(type(b_data))  # bytes类型
print(b_data)        # b'\xe6\xb2\xa7\xe6\xba\x90\xe8\xbf\x9c'

print('-' * 30)
str_data = b_data.decode()
print(type(str_data))    # str类型
print(str_data)          # 沧源远

"""

str可以通过encode方法转换成bytes类型
同样bytes类型也可以通过decode方法转换成str类型

在读取文件写入文件的过程中, 要通过二进制的方式读写的话,要在'w', 'r', 'a'后面加上b, 如'wb', 'rb', 'ab'

"""