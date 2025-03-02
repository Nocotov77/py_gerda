str1 = input()
str2 = input()
comp = input()

if comp == ">":
    if str1 > str2:
        print(str1)
    else:
        print(str2)
elif comp == "<":
    if str1 < str2:
        print(str1)
    else:
        print(str2)