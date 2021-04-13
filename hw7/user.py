from socket import *
import sys
import time

BUF_SIZE = 1024
LENGTH = 20

while True:
    case = sys.stdin.readline().strip()

    # Device 1
    s1 = socket(AF_INET, SOCK_STREAM)
    s1.connect(('localhost', 7777))

    # Device 2
    s2 = socket(AF_INET, SOCK_STREAM)
    s2.connect(('localhost', 9000))

    # 사용자가 '1'을 입력했을 경우
    if case == '1':
        s1.send(b'Request')
        data = s1.recv(BUF_SIZE).decode().split(',')

        if not data:
            s1.close()
            sys.exit()

        now = time.strftime('%c', time.localtime(time.time()))
        device_data = now + f': Device1: Temp={data[0]}, Humid={data[1]}, lilum={data[2]}'  + '\n'
        print(device_data)

        f = open('data.txt', 'a')
        f.write(device_data)
        f.close()
    
    # 사용자가 '2'를 입력했을 경우
    elif case == '2':
        s2.send(b'Request')
        data = s2.recv(BUF_SIZE).decode().split(',')

        if not data:
            s2.close()
            sys.exit()

        now = time.strftime('%c', time.localtime(time.time()))
        device_data = now + f': Device2: Heartbeat={data[0]}, Steps={data[1]}, Cal={data[2]}' + '\n'
        print(device_data)

        f = open('data.txt', 'a')
        f.write(device_data)
        f.close()

    # 사용자가 'quit'을 입력했을 경우
    elif case == 'quit':
        s1.send(b'quit')
        s2.send(b'quit')
        s1.close()
        s2.close()
        break        