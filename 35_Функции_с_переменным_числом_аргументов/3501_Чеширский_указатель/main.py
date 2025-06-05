s = input()
words = s.split()
start, *middle, end = words
low = start.lower()
high = end.lower()
res = [word for word in middle if low <= word.lower() <= high]
print(*res)