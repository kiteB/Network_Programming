from socket import *
import random
import time

BUFSIZE = 1024
port = 3333

sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', port)

while True:
    # 송신 측
    msg = input("-> ")
    reTx = 0

    while reTx <= 3:    # 최대 3회 재전송
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)  # 2초 타임아웃 설정

        try:
            data = sock.recv(BUFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break    
    
    if reTx > 3:    # 최대 3회 재전송이므로, 3을 넘어가면 timeotu 출력
        print("Timeout")
    
    # 수신 측
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFSIZE)
        if random.random() <= 0.5:  # 50%의 확률로 'ack'을 보내지 않음.
            continue
        else:
            sock.sendto(b'ack', addr)
            print("<-", data.decode())
            break
