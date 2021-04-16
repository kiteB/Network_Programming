# TCP 서버용 사용자 모듈 작성
# 소켓 생성과 연결을 모듈로 구현
# 이후, TCP 서버 프로그램 구현 시 재사용 가능
class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)

    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr 

if __name__ == "__main__":
    sock = TCPServer(9999)
    c, addr = sock.Accept()
    print('connected by ', addr)
    c.send(b'Hello Client')
    c.close()
