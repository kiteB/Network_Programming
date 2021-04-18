# UDP 손실 복구 프로그램
# 전송 손실을 가정한 UDP 서버 프로그램
# 30%의 데이터 손실이 발생한 것으로 가정하여 수신 데이터 중에서 70%에 대해서만 응답을 전송한다.
from socket import *
import random

BUFSIZE = 1024
port = 5555

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening...')

while True:
    data, addr = s_sock.recvfrom(BUFSIZE)
    if random.randint(1, 10) <= 3:  # 30%의 데이터 손실 가정
        print('Packet from {} lost!'.format(addr))
        continue
    print('Packet is {} from {}'.format(data.decode(), addr))

    s_sock.sendto('ack'.encode(), addr)