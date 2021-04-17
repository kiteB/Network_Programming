# UDP 에코 서버
# 클라이언트로부터 수신한 데이터를 출력하고, 상대방에게 다시 전송
# 연결 설정이 없으므로, 다수의 사용자와 송수신 가능
from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUFSIZE)
    print("Received: ", msg.decode())

    sock.sendto(msg, addr)