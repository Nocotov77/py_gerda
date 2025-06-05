from collections import defaultdict
vessels = []
current = []
while True:
    line = input().strip()
    if not line:
        if current:
            vessels.append(set(current))
        break
    num = int(line)
    if num == -1:
        if current:
            vessels.append(set(current))
            current = []
    else:
        current.append(num)
if current:
    vessels.append(set(current))

count = defaultdict(int)
for vessel in vessels:
    for num in vessel:
        count[abs(num)] += 1

result = [str(k) for k, v in count.items() if v == 1]
print(' '.join(result))