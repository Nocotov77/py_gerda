prev = 0
count = 0
num = int(input())

while True:
    prev = num
    num = int(input())
    if num == 0:
        break
    if num > prev:
        count += 1

print(count)