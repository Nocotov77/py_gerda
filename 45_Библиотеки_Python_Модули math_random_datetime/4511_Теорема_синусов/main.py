import math


a = float(input())
b = float(input())
c = float(input())
sinC = float(input())
A = math.degrees(math.asin(a * sinC / c))
B = math.degrees(math.asin(b * sinC / c))
print(A)
print(B)