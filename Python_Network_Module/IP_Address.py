# IP 주소 변환
# inet_aton() : 문자열 주소를 4바이트 bytes 객체로 변환
# inet_ntoa() : 4바이트 bytes 객체를 문자열 주소로 변환
import binascii
import socket
import sys

for string_address in ['114.71.229.95']:
    packed = socket.inet_aton(string_address) 
    print('Original: ', string_address)
    print('Packed: ', binascii.hexlify(packed))     # binascii.hexlify() : 16진수로 보여주는 함수 
    print('Unpacked: ', socket.inet_ntoa(packed))


# 실행 결과
# Original:  114.71.229.95
# Packed:  b'7247e55f'
# Unpacked:  114.71.229.95