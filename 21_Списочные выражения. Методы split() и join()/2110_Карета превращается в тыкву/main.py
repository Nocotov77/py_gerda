text = input()
print(' '.join(' '.join([word for word in text.split()])[::-1].split()[::-1]))