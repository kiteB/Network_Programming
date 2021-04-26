# 공유 자원을 사용하는 프로그램 : 클라이언트
from socket import *

port = 2500
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', port))

print(int(s.recv(BUFSIZE).decode()))

s.close()