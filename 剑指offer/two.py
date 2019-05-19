# 实现单例

"""使用new方法， 将类的实例绑定在类变量上，判断是否为none，

如果没有的话，new一个该类的实例并返回，没有的话直接返回类变量"""


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            singer = super(Singleton, cls)
            cls._instance = singer.__new__(cls, *args, **kwargs)
        return cls._instance


class TestClass(Singleton):
    a = 1


one = TestClass()
two = TestClass()

print(id(one))
print(id(two))


"""使用装饰器实现"""


def singleton(cls, *args, **kwargs):
    instance = {}

    def get_instance():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class TestClass2:
    a = 1


three = TestClass2()
four = TestClass2()

print(id(three))
print(id(four))

