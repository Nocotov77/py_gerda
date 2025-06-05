from math import floor

n = int(input())

n1 = floor(n / 100 % 10)
n2 = floor(n / 10 % 10)
n3 = floor(n % 10)

if n1 > n2:
    print(n1 - n2)
else:
    print(n3)