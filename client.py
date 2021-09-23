import socket
from time import sleep

import socket
# Создать сокет
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
    send_msg=input("Ты написал:")
    # Используйте этот сокет для кодирования того, что вы вводите, и отправьте его на этот адрес и соответствующий порт
    client.sendto(send_msg.encode('utf-8'),('localhost',50000))
    if send_msg=='q':
        break
    # Декодировать полученную информацию
    back_msg=client.recv(1024).decode('utf-8')
    # Печать декодированной информации
    print(back_msg)
client.close()