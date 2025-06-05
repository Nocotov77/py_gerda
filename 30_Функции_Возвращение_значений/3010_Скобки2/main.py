def brackets(line):
    mapping = {')': '(', ']': '[', '}': '{', '>': '<'}
    stack = []
    for ch in line:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
    return not stack