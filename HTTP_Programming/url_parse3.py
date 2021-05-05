# URL 결합하기
from urllib import parse

# urljoin(base, url[]): base와 url을 결합해 URL 생성
iot_url_1 = parse.urljoin('https://labs.sch.ac.kr','department/iot')
print('IoT Homepage 1: ', iot_url_1)

iot_url_2 = 'https://labs.sch.ac.kr/'+'department/iot'
print('IoT Homepage 2: ', iot_url_2)

# iot 대신 bigdata로 변환
big_url = parse.urljoin(iot_url_1, 'bigdata')
print("Bigdata Homepage: ", big_url)

p_url = parse.urlparse(iot_url_1)
print("Parsed URL: ", p_url)

# geturl(): urllib.parse.urlparse() 함수로부터 분해된 URL 요소를 하나의 URL로 결합
print("Unparsed URL: ", p_url.geturl())

# urlparse(parts): 튜플 parts로부터 URL 구성
url = parse.urlunparse(p_url)
print("Encoded: ", url)