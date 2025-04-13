list1 = []
count = 0

while True:
    num = int(input())
    count += 1
    if abs(num) >= 1000:
        break
    list1.append(num)

list1.sort(reverse=True)
print(list1[1])