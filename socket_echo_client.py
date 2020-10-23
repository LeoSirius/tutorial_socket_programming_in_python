# socket_echo_client.py
import socket

HOST = '39.106.229.224'  # server ip
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world!!!')
    data = s.recv(1024)

print('received: {}'.format(data))