n = int(input())
waves = []
for _ in range(n):
    parts = input().split()
    score = int(parts[-1])
    description = ' '.join(parts[: - 1])
    waves.append((description, score))

result = []
for i in range(len(waves) - 1):
    if waves[i][1] < waves[i + 1][1]:
        result.append((i + 1, waves[i][0]))

for item in result:
    print(f"({item[0]}, '{item[1]}')")