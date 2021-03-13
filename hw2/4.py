# 숫자를 문자열로 변환하는 방법은 str(num)을 이용한다. str(12) -> '12'가 된다.
# 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다. int('12') -> 12가 된다.
# 이를 이용하여 1부터 1000까지의 숫자의 각 자릿수의 합을 모두 구하라.
# 예를 들어 234 -> 2+3+4 = 9
import sys

sum = 0

for i in range(1, 1001):
    str_num = str(i)
    
    for j in str_num:
        sum += int(j)
    print('num: {}, sum: {}'.format(str_num, sum))
