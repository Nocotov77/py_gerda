import math

s = input()
n = len(s)
d = len(set(s))
print(n * math.log2(d))