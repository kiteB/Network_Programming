# 여러 사이트의 IP 주소를 확인하는 프로그램
import socket

HOSTS = [
    'www.sch.ac.kr',
    'homepage.sch.ac.kr',
    'www.daum.net',
    'www.google.com',
    'iot' 
]

for host in HOSTS:
    try:
        print('{}: {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{}: {}'.format(host, msg))


# 실행 결과
# www.sch.ac.kr: 220.69.189.98
# homepage.sch.ac.kr: 220.69.189.98
# www.daum.net: 203.133.167.81
# www.google.com: 142.250.196.132
# iot: [Errno 11001] getaddrinfo failed