n = int(input())
m = int(input())

pos = 0

while True:
    k = int(input())
    match k:
        case 0:
            break
        case 1:
            pos += n
        case -1:
            pos -= m

print(pos)