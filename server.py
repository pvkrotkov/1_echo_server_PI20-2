import socket
sock = socket.socket()
sock.bind(('localhost',10150))


while True:

    sock.listen(0)

    conn, addr = sock.accept()


    data = conn.recv(1024)
    print(addr)
    if not data:
        continue
    conn.send(data.upper())
    print(data.decode())
    if data.decode() == "close":
        conn.close()

        break
