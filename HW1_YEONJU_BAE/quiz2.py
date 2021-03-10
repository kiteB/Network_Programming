list = ['kim', 'lee', 'bae']
list.insert(0, 'park')
list.insert(2, 'choi')
list.append('han')
print(list)

numbers = [1, 2, 3]
numbers[1] = 17
numbers = numbers + [4, 5, 6]
del(numbers[0])
numbers.sort()
numbers.sort(reverse=True)
numbers[3] = 25
print(numbers)