words = input().split()
m = max(len(word) for word in words)
print(*map(lambda w: '*' * (m - len(w)) + w, words), sep='\n')