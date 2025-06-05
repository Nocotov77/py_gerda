def blade(word):
    result = [word]
    if len(word) % 2 == 0:
        while len(word) > 1:
            word = word[:-1]
            result.append(word)
    else:
        while len(word) > 1:
            word = word[1:]
            result.append(word)
    return result