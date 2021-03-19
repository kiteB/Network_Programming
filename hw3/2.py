# 아래 내용에 대한 프로그램(1개)을 작성하라.
import sys

d = [{'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}]


# 전화번호가 8로 끝나는 사용자 이름을 출력하라.
print('Solve 1')
for i in range(len(d)):
    if d[i]['phone']:
        phone = d[i]['phone']

        if phone[-1] == '8':
            print(d[i]['name'])

print()
# 이메일이 없는 사용자 이름을 출력하라
print('Solve 2')
for i in range(len(d)):
    if len(d[i]['email']) == 0:
        print(d[i]['name'])
        

print()
# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다' 라는 메시지를 출력하라.
print('Solve 3')
name = sys.stdin.readline().strip()
no_name = True

for i in range(len(d)):
    if name in d[i]['name']:
        print(d[i]['phone'], d[i]['email'])
        no_name = False

if no_name:
    print('이름이 없습니다')