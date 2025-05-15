s = input().strip()
words = []
n = len(s)
i = 0

while i < n:
    if s[i] != ' ':
        start = i
        while i < n and s[i] != ' ':
            i += 1
        words.append(s[start:i])
    else:
        while i < n and s[i] == ' ':
            i += 1

max_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        max_word = word

print(max_word)