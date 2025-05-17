n = int(input())
m = int(input())
plants = [input().strip() for _ in range(m)]
plants.sort(key=lambda x: (len(x), x))
beds = [[] for _ in range(n)]
for i, plant in enumerate(plants):
    beds[i % n].append(plant)
for bed in beds:
    print(", ".join(bed))
