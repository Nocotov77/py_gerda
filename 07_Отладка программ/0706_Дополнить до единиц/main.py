from sys import exit


def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


n = int(input())
if n == 0:
    print("1")
    exit()
text = convert_to(n, 2)
result = []

for i in range(len(text)):
    result.append(text[i])

for i in range(len(result)):
    if result[i] == '1':
        result[i] = '0'
    else:
        result[i] = '1'

result = ''.join(result)
result = int(result, 2)
print(result)