from math import sqrt

a = float(input())
b = float(input())

if a <= 0 or b <= 0:
    print('None')
else:
    print(sqrt(a ** 2 + b ** 2))