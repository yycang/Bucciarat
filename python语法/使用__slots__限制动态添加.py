##################
# __slots__魔法方法
##################

"""

动态语言支持后续不断对类补充特性, 这样比较灵活
但是如果要是限制对类的添加, 可以使用__slots__限制能添加的属性

"""


class Foo(object):
    # 允许添加的属性, 使用元组表示
    __slots__ = ("name", "age", "gender")
    pass


obj = Foo()
obj.name = '小王'
obj.hello = 'hello'
print(obj.name, obj.hello)      # 'Foo' object has no attribute 'hello'


# 但是需要注意的是, __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class Foo2(Foo):
    pass

obj2 = Foo2()
obj2.hello = 'hello'
print(obj2.hello)


# 子类中也可以使用__slots__魔法方法, 子类允许添加的属性是子类中__slots__允许的属性和父类中__slots__允许的属性
