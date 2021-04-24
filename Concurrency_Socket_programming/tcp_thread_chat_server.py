# 멀티스레드 TCP 채팅 프로그램 만들기: 채팅 서버
from socket import *
import threading

port = 3333
BUFSIZE = 1024

def sendTask(sock):
    while True:
        resp = input()
        print('->', resp)
        sock.send(resp.encode())

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1)
conn, addr = s.accept()

th = threading.Thread(target=sendTask, args=(conn,))
th.start()

while True:
    data = conn.recv(BUFSIZE)
    print('<-', data.decode())