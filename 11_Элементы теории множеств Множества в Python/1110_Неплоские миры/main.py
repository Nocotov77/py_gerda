n = int(input())
components = set()

for _ in range(n):
    m = int(input())
    for _ in range(m):
        component = input().strip()
        components.add(component)

for item in components:
    print(item)