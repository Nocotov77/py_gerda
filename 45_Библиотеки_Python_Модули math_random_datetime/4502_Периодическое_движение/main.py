import math

x = float(input())
angle = (x * 180 / math.pi) % 360
print(angle)