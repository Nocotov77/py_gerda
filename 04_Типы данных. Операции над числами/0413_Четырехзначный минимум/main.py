from math import floor

n = int(input())
a = floor(n / 1000)
b = floor(n / 100 % 10)
c = floor(n / 10 % 10)
d = floor(n % 10)

if b <= a:
    a, b = b, a
if d <= c:
    c, d = d, c
if c <= a:
    a, c = c, a
if c <= b and c <= d:
    b, c = c, b
if d <= b and d <= c:
    b, d = d, b
if d <= c:
    d, c = c, d
if a == 0 and b == 0 and c == 0:
    print(str(d) + '000')
elif a == 0 and b == 0:
    print(str(c) + '00' + str(d))
elif a == 0:
    print(str(b) + '0' + str(c) + str(d))
else:
    print(str(a) + str(b) + str(c) + str(d))