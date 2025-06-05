import math

x = int(input())
y = int(input())
r = int(input())

if r < 0:
    print(0)
else:
    count = 0
    r_sq = r * r
    for dx in range(-r, r + 1):
        dx_sq = dx * dx
        if dx_sq > r_sq:
            continue
        remaining = r_sq - dx_sq
        max_dy = math.isqrt(remaining)
        count += (max_dy * 2 + 1)
    print(count)