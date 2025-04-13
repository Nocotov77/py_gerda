tmp, s = 0, ''
for i in range(1, 6):
    k = int(input())
    if k > tmp:
        s += str(i) + ' '
        tmp = k
print(s)