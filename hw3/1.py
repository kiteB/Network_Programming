# 아래 내용에 대한 프로그램(1개)을 작성하라.
import sys

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 
        'May': 31, 'June': 30, 'July': 31, 'August': 31, 
        'September': 30, 'October': 31, 'November':30, 'December': 31}


# 사용자가 월을 입력하면 해당 월에 일수 출력
month = sys.stdin.readline().strip()
print(days[month])


# 알파벳 순서로 모든 월 출력
print(sorted(days))


# 일수가 31인 월 모두 출력
for key, val in days.items():
    if val == 31:
        print(key)


# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍 출력
for key, val in sorted(days.items(), key=lambda x: x[1]):
    print(key, val)


# 사용자가 월을 3자리만 입력하면 월의 일수 출력
month_3 = sys.stdin.readline().strip()
for key, val in days.items():
    if month_3 in key:
        print(val)
