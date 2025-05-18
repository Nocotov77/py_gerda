
min_mass = int(input())
n = int(input())
total = sum(sum(filter(lambda x: x >= min_mass, map(int, input().split()))) for _ in range(n))
print(total)
