import socket

sock = socket.socket() 
sock.bind(('', 9090)) 
sock.listen(1) 
conn, address = sock.accept()

msg = ''
while True:
    data = conn.recv(1024)
    if not data:
        break
    elif data.decode() == 'exit':
        print("Подключение прервано")
        break
    msg += data.decode() 
    conn.send(data.upper()) 

print('Полученные данные: ', msg)
conn.close()
