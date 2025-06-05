n = int(input())
s = len(input())
s1 = 0
counter = 0

for i in range(n - 1):
    s1 = len(input())
    if s1 <= s:
        counter += 1

print(f'Длина первой строки: {s}, количество подходящих строк: {counter}')