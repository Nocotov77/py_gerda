import re

n = int(input())
lines = [input().strip() for _ in range(n)]
k = int(input())
query = [input().strip() for _ in range(k)]


def clean_word(word):
    return re.sub(r'^[^a-zA-Zа-яА-Я]*(.*?)[^a-zA-Zа-яА-Я]*$', r'\1', word)


for line in lines:
    words = line.split()
    cleaned_words = [clean_word(word) for word in words]
    cleaned_set = set(cleaned_words)
    if all(q in cleaned_set for q in query):
        print(line)