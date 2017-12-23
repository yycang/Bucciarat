#################
# cookie和session
#################


"""

session: 存放在服务器上,
http是无状态的协议,也就是无法得知用户的状态,所以需要用session来识别
服务器为用户创造了session,用来追踪这个用户,得知他购物车里面有多少小黄书,这个session有唯一的标示
在服务端存放session的方式有很多,比如存在文件,内存或者数据库中
大型网站还有session服务器集群,用来保存用户会话

那么服务端如何识别到特定的用户,这时就用到了cookie

cookie: 存放在浏览器上,
每次http请求时,客户端都会发送cookie到服务端, 大多数都是用cookie来实现session应用的,
第一次创建session的时候,服务端会在cookie中记录一个session id,
如果以后浏览器禁用了cookie,也可以通过其他方式来传送session id(例如放在url中传递),
安全性能比较低,
单个cookie保存的数据不能超过4K, 浏览器还限制一个站点最多保存的cookie数

"""