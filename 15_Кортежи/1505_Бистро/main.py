n = int(input())
orders = []

for _ in range(n):
    dish = input().strip()
    found = False
    for item in orders:
        if item[0] == dish:
            item[1] += 1
            found = True
            break
    if not found:
        orders.append([dish, 1])

for dish, count in orders:
    print(f"({count}, '{dish}')")