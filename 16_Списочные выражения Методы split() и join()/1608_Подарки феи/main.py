words = input().split(", ")
n = len(words)
result = ["flower" if i % 2 == 0 else "gemstone" for i in range(n)]
print("; ".join(result))