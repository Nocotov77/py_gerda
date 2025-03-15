from math import floor

n = int(input())

a = floor(n / 100 % 10)
b = floor(n / 10 % 10)
c = floor(n % 10)

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
elif a != 0 and b != 0 and c != 0:
    print(a * b * c)
else:
    print(max(a, b, c) - min(a, b, c))