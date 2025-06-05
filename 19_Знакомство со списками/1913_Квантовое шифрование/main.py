n = int(input().strip())
m = int(input().strip())
originals = [input().strip() for _ in range(n)]
received = [input().strip() for _ in range(m)]

original_set = set(originals)
output = []

for s in received:
    digit_str = ''.join(c for c in s if c.isdigit())
    if digit_str:
        k = int(digit_str)
        if k == 0:
            continue
        if k - 1 < len(s):
            decrypted = s[k - 1:: k]
            if decrypted in original_set:
                output.append(decrypted)
                original_set.remove(decrypted)

if not output:
    print("NO")
else:
    for msg in output:
        print(msg)