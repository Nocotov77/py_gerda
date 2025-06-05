s = input()
list1 = []

while True:
    if s == "":
        break
    list1.append(s)
    s = input()

for i in range(len(list1)):
    if 100 <= len(list1[i]) <= 999:
        print(list1[i - 1])
    elif len(list1[i]) % 2 == 0:
        print(list1[i] * 2, sep="")
    elif len(list1[i]) % 3 == 0:
        print(list1[i] * 3, sep="")
    else:
        print(list1[i])