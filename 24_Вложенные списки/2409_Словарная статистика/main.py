from collections import Counter

words = []
while True:
    word = input().strip()
    if not word:
        break
    words.append(word)

result = []
for word in words:
    freq = Counter(word)
    word_freq = [freq[char] for char in word]
    result.append(word_freq)

print(result)