import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('localhost', 9090))

print('Начать чат! ')

while True:
        data, addr = socket.recvfrom(1024)
        recvmsg = data.decode('utf-8')
        if recvmsg == 'exit!':
        	print("Другой участник добровольно закончил чат с тобой, пока!")
        	break
	print('client msg: ' + recvmsg)
	replymsg = input('Ответить:')
	socket.sendto(replymsg.encode('utf-8'), addr)

socket.close()
