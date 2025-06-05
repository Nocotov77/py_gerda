def all_mixed_up(phrase):
    phrase = phrase.lower()
    words = phrase.split()
    res = {}
    longest = len(max(words, key=len, default=''))
    print(longest)
    for i in range(longest):
        letter = []
        for word in words:
            if i < len(word):
                letter.append(word[i])
        letter = sorted(set(letter), reverse= True)
        res[i] = letter

    return res