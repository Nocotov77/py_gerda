n = int(input())
first = {input().strip() for _ in range(n)}
m = int(input())
second = {input().strip() for _ in range(m)}

common = first & second
for num in common:
    print(num)