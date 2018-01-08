####
# 栈
####

"""

栈是一种容器, 可存入数据元素, 按照先进后出(LIFO)的元素访问顺序.

Stack(self)     创建空栈
is_empty(self)  判断栈是否为空, 空时返回True
push(self, item)    将item元素加入栈, 又称压入或推入
pop(self)       删除栈中最后加入的元素并返回, 常称弹出
top(self)       取得栈里最后压入的元素, 不删除

"""


class Stack(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def top(self):
        return self.item[-1]

    def length(self):
        return len(self.item)


if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(1)
    s.push(2)
    s.push(5)
    print(s.top())
    print(s.pop())
    print(s.is_empty())
    print(s.length())