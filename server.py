import socket

sock = socket.socket()
sock.bind(('', 9090))




while True:
	msg = ''
	sock.listen(0)
	conn, addr = sock.accept()
	data = conn.recv(1024)
	if not data:
		continue
	
	conn.send(data)
	print(addr,data.decode())
	if data.decode() == "close":
		break

conn.close()
