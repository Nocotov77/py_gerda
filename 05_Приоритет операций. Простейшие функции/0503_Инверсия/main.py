from sys import exit

x = float(input())

if abs(x) < 10 ** -9:
    print('INFINITELY LARGE')
    exit()
elif abs(x) > 10 ** 9:
    print('INFINITELY SMALL')
    exit()

print(1 / x)