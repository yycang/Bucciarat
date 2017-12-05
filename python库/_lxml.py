"""

lxml是一款高性能的Python HTML/XML解析器, 我们可以利用XPath, 来快速的定位特定元素以及获取节点信息

XPATH:
XML Path Language 是一门在HTML/XML文档中查找信息的语言
可以用来在 HTML/XML 文档中对元素和属性进行遍历

本笔记涉及到的内容有:
1.认识XML和HTML
2.了解XML的节点
3.XPATH节点选择
4.lxml库使用

"""

from lxml import etree


################
# 1.认识XML和HTML
################

"""

XML:    Extensible Markup Language(可扩展标记语言)
被设计为传输和存储数据, 其焦点是数据的内容
和json效果相同, 只不过json是轻量级的, 占用的数据量比较小, 所以大家都在用json

HTML:   HyperText Markup Language(超文本标记语言)
用来显示数据以及更好的显示数据

"""

###############
# 2.了解XML的节点
###############

"""
<book>
    <comic>
        <title>One Piece</title>
        <author>尾田荣一亮</author>
        <publish>1997</publish>
        <price>9.8</price>
    </comic>
</book>

节点:     上面每个XML标签都称为节点
节点关系:
Parent:     comic 元素是 title,author,publish 以及 price 元素的父节点
Children:   comic 元素是 book 元素的子节点
Sibling:    title,author,publish 以及 price 元素 互为兄弟节点
Ancestor:   title 节点的先辈 是 comic 和 book 节点
Descendant: book 的后代是 title 等节点

"""

###############
# 3.XPATH节点选择
###############

"""

XPATH节点选择工具:
Chrome插件: XPath Helper
Firefox插件: xpath Checker

XPATH节点选择语法:
nodename        选取此节点的所有子节点
/               从根节点选取
//              从匹配选择的当前节点选择文档中的节点, 而不考虑它们的位置
.               选取当前节点
..              选取当前节点的父节点
@               选取属性

在chrome插件选择标签, 选中后, 选中的标签会添加属性class="xh-highlight"

/book/comic[1]              选取book子元素的第一个comic元素
/book/comic[last()]         选取book子元素的最后一个comic元素
/book/comic[last()-1]       选取book子元素的倒数第二个comic元素
/book/comic[position()<3]   选取book子元素前两个comic元素
//title[@op]                选取所有拥有op属性的title元素
//title[@op='chi']          选取所有元素拥有值为chi的op属性的title元素
/book/comic[price>10]       book下comic元素,并且price元素的值大于10
/book/comic[price>10]/title book下comic元素的所有price值大于10的title元素

未知节点
*       匹配任何元素节点
@*      匹配任何属性节点
node()  匹配任何类型的节点

/book/*                 选取book下所有的子元素
//*                     选取文档中所有的元素
html/node()/meta/@*     选择html下面任意节点下的meta节点的所有属性
//title[@*]             选择所有带属性的title元素

选取若干路径
//book/comic | //book/novel     选取book元素的所有comic和novel元素
//title | // price              选取文档中所有title和price元素
/book/comic/title | // price    选取属于book/comic下的所有title元素和price元素


"""

#############
# 4.lxml库使用
#############

text = '''
<div>
    <ul>
        <li class="item-1"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
</div>
'''
# 上述html文本中少了一个闭合标签</li>

# 转换成element对象
html = etree.HTML(text)
print(type(html))       # <class 'lxml.etree._Element'>

# 将element对象转换成字符串
str_html = etree.tostring(html)
print(type(str_html))   # <class 'bytes'>

"""

etree.HTML()    可以将html字符串转换成element
而element可以拥有xpath的方法

注意: lxml可以修复html代码
例如上述的text少一个闭合标签, 但你再转成字符串输出的时候, 发现lxml已经自动帮你补上了

"""







