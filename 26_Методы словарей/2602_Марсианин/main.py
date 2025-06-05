n = int(input())
supplies = {}
for _ in range(n):
    k, v = input().split()
    supplies[k] = int(v)
consumptions = {}
for _ in range(n):
    k, v = input().split()
    consumptions[k] = int(v)
print(min(supplies[k] // consumptions[k] for k in supplies))
