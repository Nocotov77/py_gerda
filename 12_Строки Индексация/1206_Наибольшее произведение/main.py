s = input().strip()
max_product = 0
for i in range(len(s) - 4):
    product = 1
    for j in range(5):
        product *= int(s[i + j])
    if product > max_product:
        max_product = product
print(max_product)