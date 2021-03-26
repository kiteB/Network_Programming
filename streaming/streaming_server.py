import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10
videoFile = 'C:/Users/yeonju/Network_Programming/streaming/test.mp4'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(5)

while True:
    csock, addr = sock.accept()
    cap = cv2.VideoCapture(videoFile)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            temp = csock.recv(BUF_SIZE)

            result, imgEncode = cv2.imencode('.jpg', frame)
            data = np.array(imgEncode)
            byteData = data.tobytes()
            csock.send(str(len(byteData)).zfill(LENGTH).encode())

            temp = csock.recv(BUF_SIZE)

            csock.send(byteData)

            if cv2.waitKey(1) & 0xFF == ord('q'):   break
        else:   break

    cap.release()
    cv2.destroyAllWindows()
    csock.close()
