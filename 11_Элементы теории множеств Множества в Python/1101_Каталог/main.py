n = int(input())
seen = set()
for _ in range(n):
    name = input().strip()
    if name in seen:
        print("ДА")
    else:
        print("НЕТ")
        seen.add(name)