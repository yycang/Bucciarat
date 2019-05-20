# 从尾到头打印一个链表


class LinkNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def reversal(head):
    # 递归实现
    if head:
        if head.next:
            pass
            reversal(head.next)
        print(head.val)


def reversal2(head):
    stack = []
    node = head
    while node:
        stack.append(node.val)
        node = node.next

    while len(stack):
        print(stack.pop())


if __name__ == '__main__':
    n5 = LinkNode(val=5)
    n4 = LinkNode(val=4, next=n5)
    n3 = LinkNode(val=3, next=n4)
    n2 = LinkNode(val=2, next=n3)
    head = LinkNode(val=1, next=n2)

    # reversal(head)
    reversal2(head)


