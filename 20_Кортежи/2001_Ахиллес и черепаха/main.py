numbers = []
while True:
    num = int(input())
    if num == 0:
        break
    numbers.append(num)

sorted_numbers = []
while numbers:
    max_num = max(numbers)
    sorted_numbers.append(max_num)
    numbers.remove(max_num)

if sorted_numbers:
    print('->'.join(map(str, sorted_numbers)))
else:
    print('')