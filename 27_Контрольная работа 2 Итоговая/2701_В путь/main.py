list1 = []
while True:
    n = input()
    if int(n) < 10:
        break
    if n[len(n) - 2] != "7":
        list1.append(int(n))

print(max(list1))