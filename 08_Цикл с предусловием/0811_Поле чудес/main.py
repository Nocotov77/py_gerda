direct = 1
x = 0
y = 0

while True:
    s = input()
    if s == "СТОП":
        break
    if s == "налево":
        direct -= 1
        if direct < 1:
            direct = 4
    if s == "направо":
        direct += 1
        if direct > 4:
            direct = 1
    if s == "шаг":
        match direct:
            case 1:
                y += 1
            case 2:
                x += 1
            case 3:
                y -= 1
            case 4:
                x -= 1

print(x, y, sep=" ")