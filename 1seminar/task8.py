number = int(input())
first = number // 100
second = (number // 10) % 10
third = number % 10
print(first + second + third)