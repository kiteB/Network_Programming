# for 루프를 이용하여 다음과 같은 리스트를 생성하라.
# - 0 ~ 49까지의 수로 구성되는 리스트
# - 0 ~ 49까지 수의 제곱으로 구성되는 리스트
import sys

numbers = []
squared_numbers = []

for i in range(50):
    numbers.append(i)
    squared_numbers.append(i**2)

print(numbers)
print(squared_numbers)