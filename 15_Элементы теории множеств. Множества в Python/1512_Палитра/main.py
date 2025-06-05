from collections import defaultdict

color_counts = defaultdict(int)

n = int(input())
for _ in range(n):
    m = int(input())
    for _ in range(m):
        color = input().strip()
        color_counts[color] += 1

duplicate_colors = 0
total_occurrences = 0

for color, count in color_counts.items():
    if count >= 2:
        duplicate_colors += 1
        total_occurrences += count

print(duplicate_colors, total_occurrences)