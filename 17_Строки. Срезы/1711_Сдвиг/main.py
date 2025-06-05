s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    n = len(s1)
    for k in range(n):
        if s2[k:] + s2[:k] == s1:
            print(k)
            exit()
    print("NO")