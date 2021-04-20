# 서버 프로그램 
# 1. 메시지 수신 처리 부분
# 클라이언트로부터 메시지 수신 후 50% 확률로 응답하지 않는다. (메시지 손실)
# 손실되지 않은 경우, 'ack' 응답을 보내고, 화면에 채팅 메시지 출력

# 2. 메시지 송신 처리 부분
# 사용자로부터 채팅 메시지를 입력 받음.
# 재전송 횟수가 3번 이하인 경우, 메시지 전송
# 타임아웃 시간을 2초로 설정하고, 'ack' 응답을 기다림.
# 타임아웃이 발생할 경우, 재전송 횟수를 1 증가시키고, 재전송
from socket import *
import random
import time

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    # 수신
    sock.settimeout(None)   # 소켓의 블로킹 모드 timeout 설정
    
    while True:             # None인 경우, 무한정 블로킹됨.
        data, addr = sock.recvfrom(BUFSIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<-', data.decode())
            break

    # 송신
    msg = input('-> ' )
    reTx = 0
    while reTx <= 3:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)  # 소켓의 timeout 설정, 해당 timeout 내 메시지 수신을 못하면 timeout 예외 발생

        try:
            data, addr = sock.recvfrom(BUFSIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break