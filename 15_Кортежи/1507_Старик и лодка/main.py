n = int(input())
results = []

for line_idx in range(n):
    line = input().strip()
    for char_idx in range(1, len(line)):
        if line[char_idx] < line[char_idx - 1]:
            results.append((line_idx, char_idx))

for coord in results:
    print(f"({coord[0]}, {coord[1]})")