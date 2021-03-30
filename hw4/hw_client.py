import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

# 이름 문자열로 전송
sock.send(b'BaeYeonju')
# 학번 수신 후 출력
msg = sock.recv(1024)
print(int.from_bytes(msg, 'big'))
sock.close()