s = input().strip()
stack = []
pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
for char in s:
    if char in pairs.values():
        stack.append(char)
    elif char in pairs:
        if not stack or stack[-1] != pairs[char]:
            print("NO")
            exit()
        stack.pop()
    else:
        print("NO")
        exit()
print("YES" if not stack else "NO")