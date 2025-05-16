r0 = int(input())
f0 = int(input())
n = int(input())

for i in range(n):
    r = int(input())
    force = f0 * (r0 ** 2) / (r ** 2)
    print(f"('№{i + 1}', {force})")