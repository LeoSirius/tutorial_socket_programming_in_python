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
