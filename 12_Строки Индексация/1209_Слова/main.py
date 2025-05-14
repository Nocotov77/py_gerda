words = []
current_word = ''
for char in input():
    if char == ' ':
        if current_word:
            words.append(current_word)
            current_word = ''
    else:
        current_word += char
if current_word:
    words.append(current_word)

for word in words:
    print(word)