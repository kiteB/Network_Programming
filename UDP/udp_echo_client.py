# UDP 에코 클라이언트
# 서버로 메시지를 전송하고, 수신 메시지를 출력
# UDP 프로토콜은 connect()와 같은 연결이 없다.
from socket import *

port = 2500 
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter a message: ')
    if msg == 'q': # 'q'를 입력하면 종료
        break
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFSIZE)
    print('Server says: ', data.decode())

sock.close()
