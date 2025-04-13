m = int(input())
n = 1

while True:
    if m == n:
        print(n)
        break
    if m % n == 0:
        print(n)
    n += 1