###########
# @property
###########

# 我们设置一个银行类, 并使用两个方法往里面存钱和查账


class Bank(object):
    __money = 0

    def set_money(self, num):
        if not isinstance(num, int):
            raise TypeError('不合法')
        if num <= 0:
            raise ValueError('数值不正确')
        Bank.__money += num

    def get_money(self):
        return Bank.__money


# bank = Bank()
# bank.set_money(100)
# print(bank.get_money())
# bank.set_money(100)
# print(bank.get_money())


# 但是每次调用方法就太繁琐了, 能不能设置成bank.money = 100, 然后查账时直接print(bank.money)就能出结果的简单方法呢


class Bank(object):
    __money = 0

    def set_money(self, num):
        if not isinstance(num, int):
            raise TypeError('不合法')
        if num <= 0:
            raise ValueError('数值不正确')
        Bank.__money += num

    def get_money(self):
        return Bank.__money

    money = property(get_money, set_money)

# bank = Bank()
# bank.money = 100
# print(bank.money)

# 成功做到了, 就是定义一个类属性, 使用property将获取值设置为get_money方法, 设置值设置成set_money方法
# 当然还有一种高大上的方法


class Bank(object):
    __money = 0

    @property
    def money(self):
        return Bank.__money

    @money.setter
    def money(self, num):
        if not isinstance(num, int):
            raise TypeError('不合法')
        if num <= 0:
            raise ValueError('数值不正确')
        Bank.__money += num

bank = Bank()
bank.money = 100
print(bank.money)
bank.money = 100
print(bank.money)

"""

property装饰器只需要将你要修饰方法名变成要操作的属性名即可

@property又创建了一个@money.setter方法, 负责使用setter方法变成属性赋值

如果不提供设置操作的话, 这样的属性就是只读属性

"""