import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

if dx == 0 and dy == 0:
    print(1)
else:
    gcd = math.gcd(dx, dy)
    print(gcd + 1)