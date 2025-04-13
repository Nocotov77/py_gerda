a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

a1_upd = a1 * b2
b1_upd = b1 * a2

res1 = a1_upd - b1_upd
res2 = b2 * a2

i = 1
while True:
    if i >= 10000:
        break
    if res1 % i == 0 and res2 % i == 0:
        res1 /= i
        res2 /= i
        i = 1
    i += 1

print(int(res1), int(res2), sep="/")