import socket

sock = socket.socket()
sock.bind(('', 9090))

while True:
	msg = ''
	sock.listen(1)
	conn, addr = sock.accept()
	print(addr)
	data = conn.recv(1024)
	if not data:
		continue
	msg += data.decode()
	conn.send(data)

	print(msg)

	if data.decode() == "exit!":
		break
