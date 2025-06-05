n = 0
words = []
string = ''
gandalf = True

while gandalf:
    string = input()
    if 'Гэндальф' in string:
        gandalf = False
    words.append(string)
    n += 1

count = 0

for i in range(n):
    if 'волшебн' in words[i]:
        count += len(words[i])

print(count)
