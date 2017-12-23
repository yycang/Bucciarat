##########
# 并发与并行
##########

"""

首先理解一个词叫'多任务', 很容易理解, 就是你一边打开qq聊天, 一边打开网易云音乐听音乐, 一边逛淘宝买东西
这些任务都在后台悄悄的运行着

虽然现在多核cpu已经普及, 在当年单核cpu的时代是如何完成多任务的呢, 就是每个任务在cpu执行的时间非常少,
任务1来运行0.01秒, 任务2来运行0.01秒, 就这样交替执行下去, 专业名词叫'时间片轮转', 运行间隔非常小看上去像是在一起运行的

以上多任务数量大于cpu核数的情况就叫并发
而cpu核数大于等于多任务的情况就叫并行

"""

###################
# 多进程创建---1.fork
###################
import os

# fork()函数, 返回两个进程, 子进程返回0, 父进程返回子进程的id
print('process %s, start!' % os.getpid())

ret = os.fork()

if ret == 0:
    print('im %s, my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('im parent, %s' % os.getpid())    # os.getpid()获取当前进程的id, 而os.getppid()是获取子进程的父进程的id

# fork()存在于unix系统中, 而windows系统中并没有这么个玩意儿
# 当子进程被创建后, 完成了相应的任务, 就应该被父进程进行回收, 否则会有不必要的资源浪费

pid, result = os.wait()     # os.wait()会对子进程进行回收, 返回两个值, 第一个是回收的子进程id, 第二个为回收状态, 成功返回0

# 孤儿进程: 当父进程先结束, 子进程还未完成任务时, 称为孤儿进程, 但是子进程会被其他进程所收养, 所以不会有什么问题
# 僵尸进程: 当子进程先结束, 父进程却没有及时回收子进程时, 称为僵尸进程, 子进程这样会占用系统资源, 造成资源的浪费

# 在多个进程中, 势必要涉及到变量问题, 在多进程中每个资源的变量以及全局变量全部都相互独立, 互不干扰

# 多次fork, 一次fork则会生成一个父进程, 一个子进程, 再fork一次, 原先的父进程和子进程又会分别生出两个, 就好像数据结构中的二叉树一样


##############################
# 多进程创建---2.multiprocessing
##############################

"""

fork由于不能在windows中运行, 但如果要在windows中编写多进程的话, 当然会有方法支持了

multiprocessing模块提供了一个Process类来代表一个进程对象

下面来自廖雪峰博客中的一个例子

"""

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    # 参数有target为进程实例调用的对象, args和kwargs为向对象传入的可变参数,
    # name为当前创建的实例别名, 默认为Process-N, N为一个从1开始递增的数

    print('Child process will start.')
    p.start()   # 常用方法, start开始进程实例, 如果实例中没有target这个参数, 则调用run()方法
    p.join()    # 用来阻塞等待, 可以给个参数, 单位为s, 即等待x秒如果子进程还未结束, 父进程继续往下执行
    # 方法还有is_alive()判断实例是否执行, 返回布尔值,
    # terminate()强制终止进程
    print('Child process end.')


########
# 进程池
########

# 如果要创建大量的子进程, 可以用到进程池

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
        # 使用非阻塞的方式调用long_time_task, args或kwargs可以跟传入的相关参数
        # 使用阻塞的方式调用为p.apply(long_time_task, args=(i,)), 这样必须等待上一个子进程执行完才能继续执行接下来的子进程
    print('Waiting for all subprocesses done...')
    p.close()       # 关闭进程池, 不让其接新任务, terminate()为强制终止子进程
    p.join()        # 主进程阻塞, 等待所有子进程结束, 必须放在close()后用
    print('All subprocesses done.')


############
# 进程间的通信
############

# 进程间的数据要进行相互传递, 比如以爬虫为例, 一个进程从网上抓数据, 一个进程进行解析, 一个进程进行存储, 这之间数据肯定要在多个进程间进行流通的
# 下面还是廖雪峰大大博客中的一个小demo, 注释里面写笔记

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()                 # 括号中可以传值, 指定接收的最大的队列数量, 如果没有值则无上限
    # q.qsize()     返回当前队列包含的消息数量
    # q.empty()     判断队列是否为空,返回一个布尔值
    # q.full()      判断队列是否满了,返回一个布尔值

    # q.get(block, timeout)     获取队列中一条信息, 然后将其从队列中移除, block参数默认为True
    # 如果block参数为True,且没有设置超时时间timeout, 在消息队列为空的时候, 会一直等待着获取数据
    # 如果设置了timeout, 则会等待多少秒, 如果等完了发现队列中还是没有数据可以拿, 则抛出Queue.Empty异常
    # 如果block参数设置为False, 消息队列为空的时候, 才不会等待, 会立即抛出异常, 相当于q.get_nowait()

    # q.put(item, block, timeout), 将item写入消息队列, item可以为任意对象, block参数默认为True
    # 如果没有空间可以写入了, 即在q=Queue(3)设置最大消息队列为3个, block为True的情况下会等待数据被get拿走, 然后再添加
    # 设置timeout的话, 即等待x秒后, 如果还是满的, 则会抛出Queue.Full异常
    # 如果block设置为False, 消息队列满了的话会立刻抛出异常, 一点儿都不会等, 相当于q.put_nowait(item)

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
