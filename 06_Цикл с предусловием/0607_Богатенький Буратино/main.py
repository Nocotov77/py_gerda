cost = int(input())
money = 1
count = 0

while True:
    if money >= cost:
        break
    money *= 10
    count += 1

print(count)