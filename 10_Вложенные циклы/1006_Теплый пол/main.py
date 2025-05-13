n = int(input())
m = int(input())

cols = max(n, m)
rows = min(n, m)

for i in range(1, rows + 1):
    line = ""
    if i % 2 == 1:
        start = (i - 1) * cols + 1
        end = start + cols
        for j in range(start, end):
            line += f"{j}\t"
    else:
        start = i * cols
        end = start - cols
        for j in range(start, end, -1):
            line += f"{j}\t"
    line = line.rstrip("\t")
    print(line)