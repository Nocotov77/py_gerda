import sys

lines = list(sys.stdin.read().splitlines())
list_sort = []
list2 = []

for i in range(len(lines)):
    string = lines[i]
    list_sort.append(string.split())
for i in range(len(list_sort)):
    list2.append([])
    for j in range(len(list_sort[i])):
        list_sort[i][j] = int(list_sort[i][j])
        if list_sort[i][j] % 7 == 0:
            list2[i].append(list_sort[i][j])

mx = 0
index = -1
for i in range(len(list2)):
    if mx < len(list2[i]):
        mx = len(list2[i])
        index = i

print(*list2[index], sep=", ")