max_classes = int(input())

data = []
while True:
    try:
        line = input()
        if line == '':
            break
        data.extend(map(int, line.split()))
    except EOFError:
        break

parallel_data = [[] for _ in range(11)]
for i in range(11):
    for j in range(max_classes):
        index = i + j * 11
        if index < len(data):
            parallel_data[i].append(data[index])
        else:
            parallel_data[i].append(0)

averages = []
for i in range(11):
    non_zero = [x for x in parallel_data[i] if x > 0]
    if non_zero:
        avg = sum(non_zero) / len(non_zero)
        averages.append((i + 1, avg))

min_parallel = min(averages, key=lambda x: (x[1], x[0]))[0]
max_parallel = max(averages, key=lambda x: (x[1], x[0]))[0]

print(min_parallel, max_parallel)