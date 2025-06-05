from math import floor

n = int(input())

n1 = floor(n / 100 % 10)
n2 = floor(n / 10 % 10)
n3 = floor(n % 10)

raz = abs(n2 - n3)

if n1 % 2 != 0 and raz % 3 != 0:
    print('Одолеют')
else:
    print(n1, raz, sep=' ')
