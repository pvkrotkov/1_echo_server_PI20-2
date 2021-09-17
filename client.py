import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

msg = input("Введите сообщение которое хотите отправить:\n")

sock.connect(('localhost', 9090))
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
