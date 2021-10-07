import socket


while True:
     sock = socket.socket()
     sock.connect(('localhost', 10150))
     my_massage = input("Введите ваше сообщение: ")
     sock.send(my_massage.encode())

     data = sock.recv(1024)
     data = data.decode()
     print(data)
     sock.close()
