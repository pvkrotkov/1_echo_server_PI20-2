import socket
from time import sleep

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("You: ")
    client.sendto(msg.encode('utf-8'), ('localhost', 9090))
    if msg == 'exit!':
        break
    lastmsg = client.recv(1024).decode('utf-8')
    print("Server: " + lastmsg)
client.close()
