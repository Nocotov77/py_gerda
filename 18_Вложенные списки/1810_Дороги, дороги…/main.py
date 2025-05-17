roads = []
while True:
    s = input().strip()
    if not s:
        break
    roads.append(s)

cities = set()
for road in roads:
    cities.add(road[0])
    cities.add(road[1])
sorted_cities = sorted(cities)

n = len(sorted_cities)
matrix = [[0] * n for _ in range(n)]
city_index = {city: idx for idx, city in enumerate(sorted_cities)}

for road in roads:
    start, end = road[0], road[1]
    i = city_index[start]
    j = city_index[end]
    matrix[i][j] = 1

header = '  ' + ' '.join(sorted_cities)
print(header)

for i in range(n):
    row = [sorted_cities[i]] + list(map(str, matrix[i]))
    print(' '.join(row))
