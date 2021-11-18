import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    n = input()
    sock.send(n.encode())
    data = sock.recv(1024)
    print (data.decode())
    if n == "exit":
        break
sock.close()