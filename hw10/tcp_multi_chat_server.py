import socket
import time
import threading

clients = []    # 클라이언트 목록
port = 9999
BUFFSIZE = 1024


def sendTask(sock):
    while True:
        data = sock.recv(BUFFSIZE)

        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if sock in clients:
                print(sock, 'exited')
                clients.remove(sock)
                continue
                
        print(time.asctime() + str(sock) + ':' + data.decode())

        # 모든 클라이언트에게 전송
        for client in clients:
            if client != sock:
                client.send(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(10)

print('Server Started')

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print('new client', addr)
    threading.Thread(target=sendTask, args=(conn,)).start()