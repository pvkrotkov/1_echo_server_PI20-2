import socket
chat = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
chat.bind(('localhost', 9090))
print('Start chat ')
data, addr = chat.recvfrom(1024)
    revers = data.decode('utf-8')
    if revers == 'exit!':
        print("Chat stopped")
        break
    print('User: ' + revers)
    reply = input('Send: ')
    chat.sendto(reply.encode('utf-8'), addr)
chat.close()
