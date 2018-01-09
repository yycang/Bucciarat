######
# 队列
######


"""

队列只允许在一端进行插入操作, 而在另一端进行删除操作, 即先进先出的原理(FIFO, First In First Out).

Queue(self)     创建空队列
is_empty(self)  判断队列是否为空, 空时返回True
enqueue(self, item)     将元素elem加入队列, 常称为入队
dequeue(self)           删除队列中最早进入的元素并将其返回, 常称为出队
size(self)      返回队列中元素的个数

"""


class Queue(object):
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(8)
    q.enqueue(11)
    print(q.dequeue())



"""

双端队列:   双端队列中的元素可以从两端弹出, 限定插入和删除在表的两端进行, 可以从队列中任意一段入队和出队

Deque()         创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item)  从队尾加入一个item元素
remove_front()  从队头删除一个item元素
remove_rear()   从队尾删除一个item元素
is_empty()      判断双端队列是否为空
size()          返回队列的大小

"""


class Deque(object):
    def __init__(self):
        self.item = []

    def add_front(self, item):
        self.item.insert(0, item)

    def add_rear(self, item):
        self.item.append(item)

    def remove_front(self):
        return self.item.pop(0)

    def remove_rear(self):
        return self.item.pop

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)
