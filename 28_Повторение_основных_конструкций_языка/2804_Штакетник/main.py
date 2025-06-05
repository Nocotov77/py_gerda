s = input()
sep = input()
n = int(input())
chunks = [s[i: i + n] for i in range(0, len(s), n)]
print(sep.join(chunks))