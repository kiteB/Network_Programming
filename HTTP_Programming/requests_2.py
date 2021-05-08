# requests 모듈 : POST
import requests

url = 'https://httpbin.org/post'     # 요청을 JSON 형태로 돌려주는 사이트
data = {'IoT': '2017'}
rsp = requests.post(url, data=data)
print(rsp.text)
rsp = requests.post(url, json=data)
print(rsp.text)
files = {'file': open('iot.png', 'rb')}
rsp = requests.post(url, files=files)
print(rsp.text)