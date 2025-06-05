while True:
    n = int(input())
    if n == 0:
        break
    if n % 3 == 0 and n % 7 == 0:
        print("Караул!")
        break
    if n % 7 == 0:
        print("опасное")
        continue
    if n % 3 == 0:
        print("несчастливое")
        continue
    print(n)