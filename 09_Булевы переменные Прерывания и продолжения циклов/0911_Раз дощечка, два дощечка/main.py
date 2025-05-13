n = int(input())
i = 0

while True:
    line = input()
    if line == "КОНЕЦ" or i == n:
        break
    if "дос" in line or "дощ" in line:
        i += 1
        print(f"Прибили {i} дощечку.")

if i < n:
    print("МАЛОВАТО")
else:
    print("ГОТОВО")