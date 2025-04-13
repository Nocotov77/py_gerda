counter = 0
n = int(input())
goal = int(input())

while True:
    if n == goal:
        print(counter)
        break
    if counter > 1000:
        print("IMPOSSIBLE")
        break
    n /= 2
    counter += 1