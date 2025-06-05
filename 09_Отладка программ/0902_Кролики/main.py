from sys import exit

fib = [0, 1]
i = 2
A = int(input())

if A == fib[0]:
    print("0")
    exit()
if A == fib[1]:
    print("1")
    exit()

while True:
    fib.append(fib[i - 1] + fib[i - 2])

    if fib[i] == A:
        print(i)
        break
    i += 1

    if i == 1000:
        print("НЕТ")
        break
