def crypt(alphabet, line, word):
    L = len(alphabet)
    res = []
    for i, char in enumerate(line):
        idx = alphabet.index(char)
        k = alphabet.index(word[i % len(word)])
        res.append(alphabet[(idx + k) % L])
    return "".join(res)

def decrypt(alphabet, message, word):
    L = len(alphabet)
    res = []
    for i, char in enumerate(message):
        idx = alphabet.index(char)
        k = alphabet.index(word[i % len(word)])
        res.append(alphabet[(idx - k) % L])
    return "".join(res)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
line = 'ENCRYPTION'
word = 'NUMBER'
result = crypt(alphabet, line, word)
print(result)
print(decrypt(alphabet, result, word))