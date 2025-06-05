s = input().rstrip("\n")
if not s:
    exit()
words = s.split()
blocks = []
for w in words:
    L = len(w)
    if L % 2:
        H = L // 2 + 1
        b = []
        for k in range(H):
            row = [" "] * L
            if k == 0:
                row[L // 2] = w[L // 2]
            else:
                lpos = (L // 2) - k
                rpos = (L // 2) + k
                row[lpos] = w[lpos]
                row[rpos] = w[rpos]
            b.append("".join(row))
    else:
        H = L // 2
        b = []
        for k in range(H):
            row = [" "] * L
            if k == 0:
                lpos = L // 2 - 1
                rpos = L // 2
                row[lpos] = w[lpos]
                row[rpos] = w[rpos]
            else:
                lpos = (L // 2 - 1) - k
                rpos = (L // 2) + k
                row[lpos] = w[lpos]
                row[rpos] = w[rpos]
            b.append("".join(row))
    blocks.append(b)
maxH = max(len(b) for b in blocks)
padded = []
for b in blocks:
    L = len(b[0])
    pad = [" " * L] * (maxH - len(b))
    padded.append(pad + b)
for i in range(maxH):
    line = []
    for b in padded:
        line.append(b[i])
    print(" ".join(line))