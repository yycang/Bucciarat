#  两个栈实现一个队列


class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def delete_head(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return

        if self.stack2:
            return self.stack2.pop()
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


# 两个队列实现栈
class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue1.append(x)
        while self.queue2:
            x = self.queue2.pop(0)
            self.queue1.append(x)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue2.pop(0)


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.delete_head())
    q.push(4)
    print(q.delete_head())
    print(q.delete_head())
    print(q.delete_head())


