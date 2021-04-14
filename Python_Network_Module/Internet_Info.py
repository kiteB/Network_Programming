# 인터넷 서비스 정보 알아내기
# socket.getservbyport(port) : 포트 번호에 대한 서비스 이름을 반환
import socket

for port in [80, 443, 21, 25, 143, 993, 110, 995]:
    url = '{}://example.co.kr/'.format(socket.getservbyport(port))
    print('{:4d}'.format(port), url)


# 실행 결과
#   80 http://example.co.kr/
#  443 https://example.co.kr/
#   21 ftp://example.co.kr/
#   25 smtp://example.co.kr/
#  143 imap://example.co.kr/
#  993 imaps://example.co.kr/
#  110 pop3://example.co.kr/
#  995 pop3s://example.co.kr/