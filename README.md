# python socket 编程

> 意译自https://realpython.com/python-sockets/，python version 3.8+

- [背景](#背景)
- [socket_api_概览](#socket_api_概览)
- [TCP套接字](#TCP套接字)
- [最简单的client和server](#最简单的client和server)

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

现在实现一个最简单客户端和服务器，服务器把客户端发过来的数据原样返回。

先来实现`socket echo server`，这个程序把客户端发来的数据原样返回。

```py
# socket_echo_server.py
import socket

HOST = '0.0.0.0'
PORT = 8888

# 使用with语句，s会自动close()
# socket第一个参数是address family，确定是ip4，ip6或unix套接字等
# socket第二个参数是套接字类型，SOCK_STREAM会默认使用TCP协议

# bind 把这个socket和与特定的网络接口和端口号绑定
# 如果bind的host不是数字是hostname的话，需要从DNS服务器获取IP地址，这可能导致未定行为

# accept()返回tuple(socket, _RetAddress)
# 注意区分监听socket和连接socket。
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()             # accept的调用会阻塞
    with conn:
        print('Connected by ', addr)
        while True:
            data = conn.recv(1024)
            if not data:                # 当不再从客户端接收数据时，就停止连接
                break
            conn.sendall(data)
```

然后实现`socket echo client`

```py
# socket_echo_client.py
import socket

HOST = '39.106.229.224'  # server ip
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world!!!')
    data = s.recv(1024)

print('received: {}'.format(data))
```

接下来就运行来看下结果，首先启动服务器，它会在accept()那里阻塞不动。然后启动客户端。

服务器的输出

```py
$ python socket_echo_server.py 
Connected by  ('114.249.218.11', 57018)
```

客户端的输出

```py
$ python socket_echo_client.py 
received: b'Hello, world!!!'
```

在服务器脚本启动后，我们可以使用两个命令来查看socket状态

```
(base) root ~ # lsof -i -n | grep 8888
python     9780            root    3u  IPv4 3410518      0t0  TCP *:8888 (LISTEN)
(base) root ~ # netstat -an | grep 8888
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN  
```




