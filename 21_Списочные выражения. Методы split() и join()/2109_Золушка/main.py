substring = input()
sentence = input()
print(' '.join([word for word in sentence.split() if substring in word]))