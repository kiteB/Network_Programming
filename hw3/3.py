# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여 딕셔너리로 반환하는 함수를 포함하는 프로그램을 작성하라.
# Ex) 문자열 'led=on&motor=off&switch=off' 이고 구분 문자가 '&', '='일 때 {'led': 'on', 'motor': 'off'} 반환
import sys

string = list(map(str, sys.stdin.readline().strip().split('&')))
dictionary = dict()

for i in string:
    case = i.split('=')
    dictionary[case[0]] = case[1]
print(dictionary)
