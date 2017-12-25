##########
# 创建套接字
##########

import socket

# socket.socket(AddressFamily, Type)

# 使用socket.socket创建一个套接字, 该函数携带两个参数
# Address Family: 两种选择,
# 1是AF_INET(用于Internet进程间通信, 指定使用IPv4协议), 2是AF_UNIX(用于同一台机器上的进程间的通信)
# 实际上常用的是AF_INET
# 第二个参数是套接字类型
# SOCK_STREAM（流式套接字,主要用于TCP协议)或者SOCK_DGRAM（数据报套接字, 主要用于UDP协议)

########
# UDP编程
########

"""

UDP是一个面向无连接的运输层协议, 它不需要建立连接, 只需要发信就OK, 至于能不能准确无误发到就不知道了

所以UDP传输的数据不可靠, 但是它操作简单, 而且发送速度快, 所以不要求准确到达的数据就用UDP来进行传输

"""

# 客户端:

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('127.0.0.1', 8080)

data = input('请输入:')

while data:
    s.sendto(data.encode(), server_addr)        # sendto发送数据, 第一个参数二进制类型的数据, 第二个参数对面的地址

    print(s.recv(1024).decode('utf-8'))
# 关闭套接字
s.close()

# 服务端

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 8000))
while True:
    # 接受数据
    data, addr = s.recvfrom(1024)
    # 发送
    s.sendto('hello,%s'.encode() % addr)
    msg = data.decode()
    if msg == "quit":
        s.close()
        break

########
# TCP编程
########

"""

TCP协议相比与UDP协议, 是一种面向连接的, 可靠的, 基于字节流的传输层通信协议

tcp通信需要经过创建连接,数据传送,终止连接三个步骤(也就是经典的三次握手和四次挥手)

"""

# 客户端

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接, 参数为一个元组
s.connect(('127.0.0.1', 8080))
# 输出数据
msg = input('请输入:')
# 发送数据, 数据为二进制格式
s.send(msg.encode())
# 接受数据, 因为数据是通过分割成为报文段传送
data = []
while True:
    # 每次最多接受1K字节
    d = s.recv(1024)
    if d:
        data.append(d.decode())
    else:
        break
full_data = ''.join(data)
# 关闭套接字
s.close()

# 服务端

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定接口
s.bind(('127.0.0.1', 8000))
# 监听, 等待客户端的连接请求, 参数为等待的连接的最大数量
s.listen(5)
# 接受客户端的连接
sock, addr = s.accept()     # sock留下来为这个客户端的请求服务, addr为客户端的地址信息
while True:
    # 接受数据
    data = sock.recv(1024)
    if not data:
        break
    else:
        print('接受到的数据为%s' % data.decode())
        sock.send('thank you!\n'.encode())
# 关闭与客户端连接的套接字
sock.close()
# 关闭监听的套接字
s.close()




