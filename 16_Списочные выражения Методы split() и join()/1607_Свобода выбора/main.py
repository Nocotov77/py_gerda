delimiter, n, text = input().split(maxsplit=2)
n = int(n)
words = text.split(delimiter)
filtered_words = [word for word in words if len(set(word.lower())) >= n]
reversed_delimiter = delimiter[::-1]
result = reversed_delimiter.join(filtered_words)
print(result)