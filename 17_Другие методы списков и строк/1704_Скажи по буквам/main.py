sep = input().strip()
words = input().strip().split()
result = ' '.join([sep.join(word.upper()) for word in words])
print(result)