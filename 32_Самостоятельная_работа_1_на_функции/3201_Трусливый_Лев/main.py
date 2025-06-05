def remove_words(line, n):
    line = line.split()
    result = []
    for i in range(0, len(line), n):
        result.append(line[i])
    result = ' '.join(result)
    print(result)