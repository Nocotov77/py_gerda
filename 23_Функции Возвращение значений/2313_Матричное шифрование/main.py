def encrypt(text, n):
    L = len(text)
    pad = (n - (L % n)) % n
    text_padded = text + " " * pad
    rows = len(text_padded) // n
    res = []
    for j in range(n):
        for i in range(rows):
            res.append(text_padded[i * n + j])
    return "".join(res)

def decrypt(text, n):
    L = len(text)
    rows = L // n
    matrix = [[''] * n for _ in range(rows)]
    idx = 0
    for j in range(n):
        for i in range(rows):
            matrix[i][j] = text[idx]
            idx += 1
    res = []
    for i in range(rows):
        res.append("".join(matrix[i]))
    return "".join(res).rstrip()

print(encrypt('I love you!', 5))
print(decrypt('Ie!   ly oo vu ', 5))
