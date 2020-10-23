# python socket 编程

> 意译自https://realpython.com/python-sockets/

- [背景](#背景)
- [socket api 概览](#socketapi概览)
- [TCP套接字](#TCP套接字)

## 背景

`socket api`起源于`ARPANET`，在BSD中成为一套标准API。这几十年网络发展很快，但是底层的`socket api`却没怎么变。

`socket api`大概可以分成两部分：

- `Internet sockets`，用于网络通信
- `Unix domain sockets`，用于本地进程通信

## socket api 概览

python的`socket module`实现了`socket api`，基本上与系统调用对应。python还有`socketserver module`提供了更高层的封装。

`socket module`中主要的函数

- socket()
- bind()
- listen()
- accept()
- connect()
- connect_ex()
- send()
- recv()
- close()

## TCP套接字

创建套接字时，`socket.SOCK_STREAM`默认的协议是`TCP`，`socket.SOCK_DGRAM`默认的协议是`UDP`

TCP套接字的流程如下

![TCP套接字流程](https://s1.ax1x.com/2020/10/23/BAFz8g.jpg)

## 最简单的client和server

现在实现一个最简单客户端和服务器，服务器把客户端发过来的数据原样返回



