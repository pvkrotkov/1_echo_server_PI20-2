import socket

add = ('', 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create socket with UDP type

sock.bind(add) #Connect address and port with socket

while True:
    data, addr = sock.recvfrom(1024) #Received data and address for socket
    print(f'Received a message: {data.decode()} from the client', addr)
