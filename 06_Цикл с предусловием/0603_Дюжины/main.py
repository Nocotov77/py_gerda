from math import floor

num = int(input())

while floor(num) > 11:
    num /= 12

print(floor(num))