inv = {}
while True:
    line = input()
    if line == "":
        break
    shoe, size = line.rsplit(" ", 1)
    inv[(shoe, int(size))] = inv.get((shoe, int(size)), 0) + 1
q = int(input())
for _ in range(q):
    line = input()
    shoe, size = line.rsplit(" ", 1)
    key = (shoe, int(size))
    if inv.get(key, 0) > 0:
        print("Есть в наличии")
        inv[key] -= 1
    else:
        print("Нет в наличии")
