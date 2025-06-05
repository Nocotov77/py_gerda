char = input().strip()
code = ord(char)
if 65 <= code <= 90:
    code += 32
elif 97 <= code <= 122:
    code -= 32
print(chr(code))