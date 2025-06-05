import math

s = float(input())
v = float(input())

count = 0
while s - v > 0.01:
    s = math.sqrt((s - v) ** 2 + v ** 2)
    count += 1

print(count)