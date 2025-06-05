n = 1
s = 0
counter = 0

while n > 0:
    n = input()
    s = len(n)
    n = int(n)
    if n <= 0:
        break
    if (n % 3 == 0) and (s == 2 or s == 3):
        counter += 1

print(counter)