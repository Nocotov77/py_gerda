from math import floor

s = input()
n = int(input())
fart = 0
pens = 0
shill = 0
ster = 0

if s == 'фартинг':
    if n % 4 == 0:
        pens = n / 4
    else:
        pens = floor(n / 4)
        fart = n - pens * 4
    if pens % 12 == 0:
        shill = pens / 12
        pens = 0
    else:
        shill = floor(pens / 12)
        pens = pens - shill * 12
    if shill % 20 == 0:
        ster = shill / 20
        shill = 0
    else:
        ster = floor(shill / 20)
        shill = shill - ster * 20
elif s == 'пенс':
    pens = n
    if pens % 12 == 0:
        shill = pens / 12
        pens = 0
    else:
        shill = floor(pens / 12)
        pens = pens - shill * 12
    if shill % 20 == 0:
        ster = shill / 20
        shill = 0
    else:
        ster = floor(shill / 20)
        shill = shill - ster * 20

if ster != 0:
    print('Фунтов: ' + str(floor(ster)))
if shill != 0:
    print('Шиллингов: ' + str(floor(shill)))
if pens != 0:
    print('Пенсов: ' + str(floor(pens)))
if fart != 0:
    print('Фартингов: ' + str(floor(fart)))