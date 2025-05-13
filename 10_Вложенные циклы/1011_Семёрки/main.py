count = 0
while True:
    num = int(input())
    if num <= 0:
        break
    current = num
    while current > 0:
        remainder = current % 8
        if remainder == 7:
            count += 1
        current = current // 8
print(count)