word = input().strip()
length = len(word)
middle = length // 2

chars = [word[0], word[middle], word[-2], word[-1]]

result = []
for char in chars:
    if char.isupper():
        base = ord('A')
    else:
        base = ord('a')
    original = ord(char) - base
    shifted = (original - 3) % 26
    result.append(chr(shifted + base))

print(''.join(result))