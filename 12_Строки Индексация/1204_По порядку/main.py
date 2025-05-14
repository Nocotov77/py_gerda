s = input().strip()
for i in range(1, len(s)):
    if s[i] < s[i - 1]:
        print(s[i])
        exit()
print("(:_0_:)")