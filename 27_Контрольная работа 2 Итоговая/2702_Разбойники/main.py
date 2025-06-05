from random import shuffle

n = int(input())
result_set = set()
result_list = []
for i in range(n):
    s = input()
    s = list(s)
    for j in range(0, len(s), 3):
        s[j] = s[j].upper()
    s = "".join(s)
    result_set.add(str(s))
result_list.extend(result_set)
shuffle(result_list)
print(*result_list, sep="\n")