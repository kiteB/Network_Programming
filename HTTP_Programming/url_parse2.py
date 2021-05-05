# URL 파싱하기
# urllib.parse 모듈: urlsplit()
from urllib import parse

url = 'https://homepage.sch.ac.kr/sch/06/06050000.jsp?mode=view&article_no=20200528202911520374&pager.offset=0&board_no=20200302132057325672'
parsed_url = parse.urlsplit(url)

print(parsed_url)
print('scheme: ', parsed_url.scheme)
print('netloc: ', parsed_url.netloc)
print('path: ', parsed_url.path)
print('query: ', parsed_url.query)
print('fragment: ', parsed_url.fragment)