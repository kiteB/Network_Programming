# UDP 손실 복구 프로그램
# 손실 복구 기능을 가진 UDP 클라이언트 프로그램
# 타임아웃이 발생하면, 재전송하고 타임아웃 시간을 2배씩 증가시킨다.
# 타임아웃 시간이 2.0보다 커지면 재전송 중단한다.
# socket의 settimeout() 함수 이용
# 블로킹 소켓 연산에 시간 제한을 설정한다.
from socket import *

BUFSIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))

for i in range(10):
    time = 0.1
    data = 'Hello, IoT'
    while True:
        c_sock.send(data.encode())
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time))
        c_sock.settimeout(time)
        
        try:
            data = c_sock.recv(BUFSIZE)
        except timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            print('Response', data.decode())
            break    