f1 = int(input())
f2 = int(input())

d1 = 0
temp = f1
while temp > 0:
    temp = temp // 10
    d1 += 1

d2 = 0
temp = f2
while temp > 0:
    temp = temp // 10
    d2 += 1

if d1 != d2:
    print("НЕТ")
else:
    found = False

    if d1 == 4:
        first = f1 // 1000
        new_first = first + 1 if first != 9 else 9
        t1 = new_first * 1000 + (f1 % 1000)
    else:
        first = f1 // 10000
        new_first = first + 1 if first != 9 else 9
        t1 = new_first * 10000 + (f1 % 10000)
    if t1 == f2:
        print("ДА 1")
        found = True

    if not found:
        last = f1 % 10
        new_last = last - 1
        t2 = (f1 // 10) * 10 + new_last
        if t2 == f2:
            print("ДА 2")
            found = True

    if not found:
        if d1 == 4:
            last = f1 % 10
            rest = f1 // 10
            t3 = last * 1000 + rest
        else:
            last = f1 % 10
            rest = f1 // 10
            t3 = last * 10000 + rest
        if t3 == f2:
            print("ДА 3")
            found = True

    if not found:
        if d1 == 4:
            first = f1 // 1000
            rest = f1 % 1000
            t4 = rest * 10 + first
        else:
            first = f1 // 10000
            rest = f1 % 10000
            t4 = rest * 10 + first
        if t4 == f2:
            print("ДА 4")
            found = True

    if not found:
        print("НЕТ")