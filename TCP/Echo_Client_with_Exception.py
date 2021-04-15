# TCP 에코 클라이언트에 예외처리를 추가한 클라이언트 프로그램
from socket import *

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        bytesSent = s.send(msg.encode())
    except:
        print('connection closed')
        break
    else:
        print("{} bytes send".format(bytesSent))

    try:
        data = s.recv(BUFSIZE)
    except:
        print("connection closed")
    else:
        if not data:
            break
        print("Received message: %s" %data.decode())

s.close()