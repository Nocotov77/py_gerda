n = int(input())
summa = 0
quadro = 0
i = 1

while i != n + 1:
    summa += i ** 2
    quadro += i
    i += 1
quadro **= 2

print(quadro - summa)