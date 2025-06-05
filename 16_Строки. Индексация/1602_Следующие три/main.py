alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = int(input())
start = (n - 1) % 26
result = ''.join(alphabet[(start + i) % 26] for i in range(4))
print(result)