# 간단한 웹 서버: HTML 응답하기
from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_IP = 'localhost'
PORT = 8000


class http_handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<h1>Hello, IoT!</h1>')


httpd = HTTPServer((HOST_IP, PORT), http_handler)
# 로그 확인
print("Serving HTTP on {}:{}".format(HOST_IP, PORT))
# 실제로 동작시키기
httpd.serve_forever()