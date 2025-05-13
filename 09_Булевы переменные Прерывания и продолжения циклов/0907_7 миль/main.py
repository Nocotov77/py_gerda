n = int(input())
j = 0

for i in range(1, n + 1):
    j += 1
    if i % 7 == 0:
        print("Крюк!")
        j = 0
    else:
        print(f"Пройдена {j} миля.")