import sys

player = 1
s = input()
if s == "":
    print("Второй")
    sys.exit()

while True:
    prev = s
    s = input()
    if player == 1:
        player = 2
    else:
        player = 1
    if s == "" or len(s) < len(prev):
        if player == 2:
            print("Второй")
        else:
            print("Первый")
        break