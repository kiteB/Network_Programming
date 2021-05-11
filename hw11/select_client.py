import socket
import threading

port = 2500
BUFFSIZE = 1024

def handler(sock):
    while True:
        msg = sock.recv(BUFFSIZE)
        print('Received message:', msg.decode())


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

print('Port No: ', port)

data = input("Message to send1: ")
sock.send(data.encode())

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = input("Message to send: ")
    sock.send(msg.encode())