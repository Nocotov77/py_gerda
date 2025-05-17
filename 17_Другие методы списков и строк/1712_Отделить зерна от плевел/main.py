words = input().split()
letters_list = []
non_letters_list = []

for word in words:
    letters = []
    non_letters = []
    for char in word:
        if char.isalpha():
            letters.append(char.lower())
        else:
            non_letters.append(char)

    if letters:
        letters_str = ''.join(letters)
        letters_str = letters_str[0].upper() + letters_str[1:]
        letters_list.append(letters_str)

    if non_letters:
        non_letters_str = ''.join(non_letters)
        non_letters_list.append(non_letters_str)

print(' '.join(letters_list))
print(' '.join(non_letters_list))