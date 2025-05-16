number = int(input())
digits = list(map(int, str(number)))
n = len(digits)
if n == 1:
    print("NO")
    exit()

sequence = digits.copy()
found = False

while True:
    for i in range(n, len(sequence)):
        if sequence[i] == number:
            found = True
            break
    if found:
        break
    next_sum = sum(sequence[-n:])
    if next_sum > number:
        print("NO")
        exit()
    sequence.append(next_sum)
    if next_sum == number:
        found = True
        break

print(' '.join(map(str, sequence)))