import socket

add = ('', 9090)

sock = socket.socket() 

sock.connect(add) 
print('Соединение с сервером', add)

while True:
    msg = input()
    if msg == 'exit':
        break
    sock.send(msg.encode())
    print(f'Отправка данных {msg} серверу', add)
    data = sock.recv(1024)
    data_dec = data.decode()
    print(f'Прием данных {data_dec} от сервера', add)
    print(data_dec)

sock.close()
print ('Разрыв соединения с сервером', add)
