rows = []
while True:
    line = input().strip()
    if not line:
        break
    rows.append(list(map(int, line.split())))

transposed = list(zip(*rows))
transposed = [list(col) for col in transposed]

for i in range(len(transposed)):
    if i % 2 == 0:
        transposed[i].sort()
    else:
        transposed[i].sort(reverse=True)

sorted_rows = list(zip(*transposed))
sorted_rows = [list(row) for row in sorted_rows]

for row in sorted_rows:
    print('\t'.join(map(str, row)))