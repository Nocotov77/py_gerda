count = 0

while True:
    s = input()
    if " " in s:
        break
    n = int(input())
    if len(s) == n:
        count += 1

print(count)