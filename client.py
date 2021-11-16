import socket

sock = socket.socket() # создаем объект сокета
sock.setblocking(1)
sock.connect(('localhost', 9090)) # подключаемся к серверу

while True:
    msg = input('Введите сообщение: ') # клиент вводит данные
    if msg == 'exit': 
        sock.send(msg.encode())
        print("Подключение прервано")
        break
    else:
        sock.send(msg.encode())
        data = sock.recv(1024)
        print("Полученные данные: ", data.decode())

sock.close()
