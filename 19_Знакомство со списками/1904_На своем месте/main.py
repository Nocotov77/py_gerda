import bisect

n = int(input())
words = [input().strip() for _ in range(n)]
new_word = input().strip()

position = bisect.bisect_right(words, new_word)
print(position)