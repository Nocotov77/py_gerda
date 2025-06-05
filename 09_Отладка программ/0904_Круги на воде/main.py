r = int(input())
n = int(input())
m = int(input())

t = 0

while True:
    t += 1
    r -= n
    n += m
    if r <= 0:
        break

print(t)