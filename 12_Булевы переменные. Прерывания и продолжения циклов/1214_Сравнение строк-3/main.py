a, b, c = input(), input(), input()

result = (len(a) < len(b) or (len(a) == len(b) and a <= b)) and (len(a) < len(c) or (len(a) == len(c) and a <= c)) \
    and a or (len(b) < len(a) or (len(b) == len(a) and b <= a)) and (len(b) < len(c) or (len(b) == len(c) and b <= c)) \
    and b or c

print(result)