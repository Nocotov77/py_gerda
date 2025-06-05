vowels_ru = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}


def check_char(pattern_ch, word_ch):
    word_ch_lower = word_ch.lower()
    if pattern_ch == '0':
        return word_ch_lower in vowels_ru
    elif pattern_ch == '1':
        return word_ch_lower not in vowels_ru and word_ch_lower.isalpha()
    elif pattern_ch == '?':
        return word_ch_lower.isalpha()
    else:
        return False


pattern = input().strip()
has_star = '*' in pattern
left_p, right_p = '', ''

if has_star:
    star_pos = pattern.index('*')
    left_p = pattern[:star_pos]
    right_p = pattern[star_pos + 1:]
else:
    left_p = pattern
    right_p = ''

words = []
while True:
    line = input().strip()
    if not line:
        break
    words.append(line)

matched = []

for word in words:
    valid = True
    if has_star:
        min_len = len(left_p) + len(right_p)
        if len(word) < min_len:
            continue
        for i in range(len(left_p)):
            if i >= len(word) or not check_char(left_p[i], word[i]):
                valid = False
                break
        if not valid:
            continue
        right_start = len(word) - len(right_p)
        for i in range(len(right_p)):
            pos = right_start + i
            if pos >= len(word) or not check_char(right_p[i], word[pos]):
                valid = False
                break
    else:
        if len(word) != len(left_p):
            continue
        for i in range(len(left_p)):
            if not check_char(left_p[i], word[i]):
                valid = False
                break
    if valid:
        matched.append(word)

if matched:
    for word in matched:
        print(word)
else:
    print("Есть нечего, значить!")