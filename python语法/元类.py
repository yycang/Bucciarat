###########
# metaclass
###########

"""
“元类就是深度的魔法，99%的用户应该根本不必为此操心。
如果你想搞清楚究竟是否需要用到元类，那么你就不需要它。
那些实际用到元类的人都非常清楚地知道他们需要做什么，而且根本不需要解释为什么要用元类。”
 —— Python界的领袖 Tim Peters
"""

# 元类其实是一个自定义类的东西, 用元类可以创建类, 创建一个定制的类
# 自定义一个元类, 通过我们设置的元类将原来小写的字母属性改成大写


# 元类继承于type
class upper_metaclass(type):

    def __new__(cls, class_name, class_base, class_attr):
        new_class_attr = {}

        for k, v in class_attr.items():
            # 如果是魔法属性的话, 则不对其进行更改
            if k.startswith('__') and k.endswith('__'):
                continue
            else:
                new_class_attr[k.upper()] = v

        return super().__new__(cls, class_name, class_base, new_class_attr)


class Foo(object, metaclass=upper_metaclass):
    a = 100
    b = 100

f = Foo()
print(f.a)      # 'Foo' object has no attribute 'a'
print(f.A)      # 100


"""
创建元类的步骤:
1.拦截类的创建
2.修改类
3.返回修改之后的类

这么一看还蛮简单的

"""