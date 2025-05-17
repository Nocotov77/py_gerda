numbers = list(map(int, input().split()))

levels = [numbers.copy()]

while len(levels[-1]) > 1:
    current_level = levels[-1]
    new_level = []
    for i in range(0, len(current_level), 2):
        if i + 1 < len(current_level):
            new_level.append(current_level[i] + current_level[i + 1])
        else:
            new_level.append(current_level[i] + 0)
    levels.append(new_level)

for level in reversed(levels):
    print(' '.join(map(str, level)))