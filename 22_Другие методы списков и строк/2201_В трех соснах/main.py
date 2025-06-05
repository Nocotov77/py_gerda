words = input().split()
indices = [i for i, word in enumerate(words) if word == 'сосна']
print(' '.join(words[indices[0]+1:indices[-1]]).strip() if len(indices) >= 2 else '')