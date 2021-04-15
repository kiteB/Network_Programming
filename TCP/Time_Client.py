# 타임 클라이언트
# 타임 서버에 접속하여 시간을 읽어오는 클라이언트 프로그램
from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 9999))
print("Time: ", sock.recv(1024).decode())
sock.close()