import socket

import socket
# Подобно предыдущему TCP, это просто заменить socket.SOCK_STREAM на socket.SOCK_DGRAM
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Связывающий адрес и номер порта
sock.bind(('localhost',50000))

print('Начать чат! ')
# conn, addr = fwq.accept () UDP также не требует принятия
while 1:
    data, addr = sock.recvfrom(1024)
    # Декодировать полученное сообщение
    recvmsg = data.decode('utf-8')
    # Условия завершения цикла while
    if recvmsg == 'q':
        print("Другой участник добровольно закончил чат с тобой, пока!")
        break
    # Распечатать декодированное сообщение
    print('client msg:' + recvmsg)
    replymsg = input('Ответить:')
    # Отправка сообщения, на которое вы хотите ответить, отправка полученному адресу, отправка в UDP также использует sendto
    sock.sendto(replymsg.encode('utf-8'), addr)

sock.close()