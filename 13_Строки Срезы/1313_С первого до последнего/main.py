char = input().strip()
s = input().strip()

first = -1
for i in range(len(s)):
    if s[i] == char:
        first = i
        break

last = -1
for i in range(len(s) - 1, -1, -1):
    if s[i] == char:
        last = i
        break

if first == -1:
    print(s)
elif first == last:
    print(s[first + 1:])
else:
    print(s[first + 1:last])