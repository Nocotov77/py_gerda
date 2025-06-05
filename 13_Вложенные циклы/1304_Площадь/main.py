import math

s = int(input())
for a in range(math.isqrt(s), 0, -1):
    if s % a == 0:
        print(s // a, a)