def read_set():
    s = set()
    while True:
        line = input().strip()
        if not line:
            break
        s.add(line)
    return s


set1 = read_set()
set2 = read_set()
set3 = read_set()

combined = set1 | set2 | set3

n = int(input())
result = set()
for _ in range(n):
    q = input().strip()
    if q in combined:
        result.add(q)

for item in result:
    print(item)