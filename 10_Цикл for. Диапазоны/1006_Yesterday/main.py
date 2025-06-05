sym = input()
n = int(input())
counter = 0
max_counter = 0

for i in range(n):
    s = input()
    if s == sym:
        counter += 1
        if i == n - 1:
            if counter > max_counter:
                max_counter = counter
            counter = 0
    else:
        if counter > max_counter:
            max_counter = counter
        counter = 0

print(max_counter)