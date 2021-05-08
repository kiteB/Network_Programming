# requests 모듈 : PUT
import requests

url = 'https://httpbin.org/put'     # 요청을 JSON 형태로 돌려주는 사이트
data = {'IoT': '2017'}
rsp = requests.put(url, data=data)
print(rsp.text)
rsp = requests.put(url, json=data)
print(rsp.text)
files = {'file': open('iot.png', 'rb')}
rsp = requests.put(url, files=files)
print(rsp.text)