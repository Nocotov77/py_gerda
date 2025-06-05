numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

n = len(numbers)
result = [x for x in numbers if n != 0 and x % n == 0]
print(result)