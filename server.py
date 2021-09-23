import socket

sock = socket.socket()
sock.bind(('', 9092))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

counter = 0
while True:
	data = conn.recv(1024)
	#if not data:
	#	break
	msg += data.decode()
	if counter == 0:
		print(msg)
		counter = 1
	conn.send(data)
	if data.decode() == "exit":
		break

print(msg)

conn.close()
