import socket

sock = socket.socket()

add = ('', 9090)

sock.bind(add)
print('Запуск сервера', add)

sock.listen()
print('Начало прослушивания порта', add[1])

conn, addr = sock.accept()
print('Подключение клиента', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break    
	print(f'Прием данных {data.decode()} от клиента', addr)
    conn.send(data)
    print(f'Отправка данных {data.decode()} клиенту', addr)

conn.close()
print('Отключение клиента', addr)

sock.close()
print('Остановка сервера', add)