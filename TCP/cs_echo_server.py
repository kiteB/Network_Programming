# 간단한 서버 생성 함수: create_server()
# 서버에서 TCP 소켓 생성, bind, listen을 한번에 수행해주는 함수
# socket(), bind(), listen()
from socket import *

port = 2500
BUFSIZE = 1024

sock = create_server(('', port), family=AF_INET, backlog=1)
conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    data = conn.recv(BUFSIZE)
    if not data:
        break
    print("Received message: ", data.decode())
    conn.send(data)

conn.close()