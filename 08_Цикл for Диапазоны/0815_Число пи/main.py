pi = 0.0

for i in range(int(input())):
    pi += (-1) ** i / (2 * i + 1)

print(pi * 4)