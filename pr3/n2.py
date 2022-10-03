import math
print('Введите для поиска НОД 2 числа, каждое в отдельной строке')
n = int(input())
m = int(input())
while n != m:
    if n > m:
        n -= m
    else:
        m -= n
#math.gcd
print('НОД введенных чисел = ', n)
