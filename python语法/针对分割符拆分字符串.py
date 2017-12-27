#############
# Cookbook2.1
#############


"""
场景: 我们需要将字符串拆分为不同的字段, 但是其中混杂的分隔符实在是太讨厌了!

解决方案: 首先想到的字符串对象的split()方法只能针对一个分割符进行切分, 还无法切分空格, 这时候就可以使用re模块的re.split()方法
"""

import re

line = 'asdf ghjj; asdf, adsd, qwer,    foww'

res = re.split(r'[,;\s]\s*', line)
print(res)      # ['asdf', 'ghjj', 'asdf', 'adsd', 'qwer', 'foww']


# 当使用re.split()时, 注意正则模块中的捕获组是否包含在括号中, 如果用到了捕获组, 那么匹配的文本也会包含在最终结果中

res1 = re.split(r'(,|;|\s)\s*', line)
print(res1)     # ['asdf', ' ', 'ghjj', ';', 'asdf', ',', 'adsd', ',', 'qwer', ',', 'foww']


# 上面这些多余的分割符其实说不定是有用的! 例如
res2 = res1[::2]        # ['asdf', 'ghjj', 'asdf', 'adsd', 'qwer', 'foww']
res3 = res1[1::2] + ['']    # [' ', ';', ',', ',', ',', '']
res4 = ''. join([v+d for v, d in zip(res2, res3)])      # asdf ghjj;asdf,adsd,qwer,foww


# 如果不想在结果中看到分割字符, 但仍然想用()进行分组, 使用?:指定非捕获组

res5 = re.split(r'(?:,|;|\s)\s*', line)
print(res5)     # ['asdf', 'ghjj', 'asdf', 'adsd', 'qwer', 'foww']

