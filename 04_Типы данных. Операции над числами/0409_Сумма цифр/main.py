from math import floor

n = int(input())

print(floor(n / 1000) + floor(n / 100 % 10) + floor(n / 10 % 10) + floor(n % 10))
