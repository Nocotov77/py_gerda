n = int(input())
children = [input().strip() for _ in range(n)]
m = int(input())
requests = [input().strip() for _ in range(m)]

received = set()

for name in requests:
    if name in received:
        print(f"{name}, всем по одному подарку!")
    else:
        received.add(name)
        print(f"Вот твой подарок, {name}!")