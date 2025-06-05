n = int(input())
results = {}
total_sum = 0
for _ in range(n):
    m = int(input())
    price = int(input())
    total_qty = 0
    prod = ""
    for i in range(m):
        line = input().split()
        prod = line[0]
        qty = int(line[1])
        total_qty += qty
    cost = total_qty * price
    results[prod] = (total_qty, cost)
    total_sum += cost
for prod, (qty, cost) in results.items():
    print(prod, qty, cost)
print("Всего получено " + str(total_sum) + "₽.")