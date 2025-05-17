lookup = {"name": {}, "site": {}, "phone": {}, "address": {}}
n = int(input())
for _ in range(n):
    name = input()
    site = input()
    phone = input()
    address = input()
    rec = [name, site, phone, address]
    lookup["name"][name] = rec
    lookup["site"][site] = rec
    lookup["phone"][phone] = rec
    lookup["address"][address] = rec
q = int(input())
for i in range(q):
    key = input()
    val = input()
    rec = lookup[key][val]
    for r in rec:
        print(r)
    if i < q - 1:
        print("-" * 10)
