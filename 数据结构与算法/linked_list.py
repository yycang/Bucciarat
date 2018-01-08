######
# 链表
######


"""

顺序表和链表:
顺序表的构建需要预先知道数据大小来申请连续的存储空间, 而在进行扩充时又需要进行数据的搬迁, 所以使用起来不灵活

链表结构可以利用计算机碎片化空间, 实现灵活的内存动态管理

链表:

是一种常见的基础的数据结构, 能维持数据的顺序关系, 但是不像顺序表一样连续存储数据, 而在每个节点(即数据存储单元)里
存放下一个节点的位置信息

"""

#########
# 单向链表
#########

"""

链表中最简单的一种形式, 元素域elem保存着作为表元素的数据项, 链接域保存着同一个表里下一个结点的标示

从一个链表的首节点, 从这个点出发能够找到表中的第一个元素, 和下一个结点的地址, 按照这样可以找出所有链表元素

"""


class Node(object):
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_


class SingleLinkList(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        p, n = self.__head, 0
        while p:
            n += 1
            p = p.next
        return n

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur:
            print(cur.item, end=' ')
            cur = cur.next

    def add(self, item):
        """链表头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加"""
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, p, item):
        """链表中间插入节点"""
        if p <= 0:
            self.add(item)
        elif p > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (p - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur:
            if cur.item == item:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找链表中节点是否存在"""
        cur = self.__head
        while cur:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    s = SingleLinkList()
    s.add(1)
    s.add(3)
    s.add(6)
    s.insert(1, 100)
    s.remove(3)
    print(s.search(3))
    print(s.search(100))
    s.travel()


############
# 单向循环链表
############

"""

单向循环链表指的是, 链表结束的节点的next指的不再为None, 而是指向链表的头节点

"""


class SinCycLinkedlist(object):
    """单向循环链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        count = 1
        cur = self.__head
        if not cur:
            return 0
        else:
            while cur.next != self.__head:
                count += 1
                cur = cur.next
            return count

    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item, end=' ')
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item, end=' ')

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 移到链表尾部
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head

    def insert(self, p, item):
        if p <= 0:
            self.add(item)
        elif p > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (p - 1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                if not pre:
                    temp = self.__head
                    while temp.next is not self.__head:
                        temp = temp.next
                    self.__head = cur.next
                    temp.next = self.__head
                else:
                    pre.next = cur.next

            pre = cur
            cur = cur.next
        if cur.item == item:
            if cur is self.__head:
                self.__head = None
            else:
                pre.next = self.__head

    def search(self, item):
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ == '__main__':
    sc = SinCycLinkedlist()
    print(sc.is_empty())
    print(sc.length())
    sc.add(8)
    sc.add(11)
    sc.add(4)
    sc.add(18)
    sc.append(100)
    sc.insert(1, 101)
    sc.remove(4)
    print(sc.search(8))
    print(sc.length())
    sc.travel()


#########
# 双向链表
#########


"""

比较复杂, 即每个节点有两个链接, 一个指向下一个链表(如果是最后一个节点, 指向空值), 一个指向上一个链表(如果是第一个节点, 指向空值)

"""


class DNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双向链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 1
        while cur:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur:
            print(cur.item, end=' ')
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.pre = node
            self.__head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self, p, item):
        if p <= 0:
            self.add(item)
        elif p > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            count = 0
            while count < (p - 1):
                count += 1
                cur = cur.next
            node.pre = cur
            node.next = cur.next
            cur.next.pre = node
            cur.next = node

    def search(self, item):
        cur = self.__head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self.__head
            if cur.item == item:
                if cur.next is None:
                    self.__head = None
                else:
                    cur.next.pre = None
                    self.__head = cur.next
                return
            while cur:
                if cur.item == item:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                    break
                cur = cur.next


if __name__ == '__main__':
    dl = DoubleLinkList()
    print(dl.is_empty())
    dl.add(9)
    dl.add(10)
    dl.append(100)
    dl.insert(1, -1)
    dl.remove(-1)
    print(dl.search(100))
    dl.travel()
    print(dl.length())

