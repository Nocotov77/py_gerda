s = input()
s = s.split("; ")
separate = input()
list1 = []

for i in range(len(s)):
    if not s[i].isalpha():
        list1.append(s[i])

print(separate.join(list1))