c = 2
for i in input():
    if i == 'с':
        c -= 2
    if i == 'к':
        c += 3
if c >= 0:
    print(f'1{c * '0'}')
else:
    print(f'1/1{abs(c) * '0'}')