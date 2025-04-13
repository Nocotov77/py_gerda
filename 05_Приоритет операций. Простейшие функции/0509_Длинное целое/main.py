s = input()

if '.' in s:
    separate, _ = s.split('.', 1)
    print(separate)
else:
    print(len(s))