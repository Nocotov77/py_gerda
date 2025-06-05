a = int(input())
b = int(input())
count = 0

while True:
    c = int(input())
    if c == -1:
        break
    if b > a and b > c:
        count += 1
    a, b = b, c

print(count)