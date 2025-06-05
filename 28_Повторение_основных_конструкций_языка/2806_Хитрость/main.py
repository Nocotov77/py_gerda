n = int(input())
s = input()
mirrored = s[::-1]
result = "".join(ch for ch in mirrored[::n] if ch.isalnum() or ch == " ")
print(result)