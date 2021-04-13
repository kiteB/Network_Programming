from socket import *
import os
import random

BUF_SIZE = 1024
LENGTH = 100

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(10)
print('Device 2')

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
        heartbeat = random.randint(40, 140) # 심박수 
        steps = random.randint(2000, 6000)  # 걸음수
        cal = random.randint(1000, 4000)    # 소모칼로리
        
        data = f'{heartbeat, steps, cal}'
        conn.send(data.encode())

    conn.close()