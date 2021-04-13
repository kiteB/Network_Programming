from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 100

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('Device 1')

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE)

    if not msg:
        conn.close()
        continue

    elif msg == b'quit':    # 'quit' 수신했을 때
        print('Client: ', addr, msg.decode())
        conn.close()
        continue

    elif msg == b'Request':     # 'Request' 수신했을 때
        print('Client: ', addr, msg.decode())

        # 사용자에게 데이터 전송
        temp = random.randint(0, 40)    # 온도
        humid = random.randint(0, 100)  # 습도
        lilum = random.randint(70, 150)  # 조도

        data = f'{temp, humid, lilum}'
        conn.send(data.encode())

    conn.close()