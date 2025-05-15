number = input().strip()
k = int(input())

max_product = 0

for i in range(len(number) - k + 1):
    current_product = 1
    substring = number[i:i + k]
    for c in substring:
        current_product *= int(c)
    if current_product > max_product:
        max_product = current_product

print(max_product)