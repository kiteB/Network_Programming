# select()를 이용한 에코 서버
# select() : 여러 개의 소켓(또는 파일)에 대해 비동기 I/O를 지원하는 함수
import socket, select

socks = []      # 소켓 리스트
BUFFER = 1024
PORT = 2500

s_sock = socket.socket()    # TCP 소켓
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)        # 소켓 리스트에 소켓을 추가
print(str(PORT) + '에서 접속 대기 중')

while True:
    # 읽기 이벤트 (요청 및 데이터 수신) 대기
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:        # 수신(읽기 가능한) 소켓 리스트 검사
        if s == s_sock:     # 새로운 클라이언트의 연결 요청 이벤트 발생
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)    # 연결된 소켓을 소켓 리스트에 추가
            print('Client ({}) connected'.format(addr))

        else:               # 기존 클라이언트의 데이터 수신 이벤트 발생
            data = s.recv(BUFFER)
            if not data:
                s.close()
                socks.remove(s)     # 연결 종료된 소켓을 소켓 리스트에서 제거
                continue

            print('Received:', data.decode())
            s.send(data)