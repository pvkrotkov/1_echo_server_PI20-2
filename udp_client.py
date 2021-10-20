import socket

add = ('', 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create socket with UDP type

while True:
    msg = input('Enter your message: ')
    if msg == 'exit':
        break
    sock.sendto(msg.encode(), add) #Sending data to server

sock.close() #Close server
