words = input().split()
if not words:
    print('\n\n')
else:
    max_len = max(len(word) for word in words)
    garland = [
        '_' + '_'.join(word[0] for word in words) + '_'
    ] + [
        ' ' + ' '.join(word[i] if i < len(word) else ' ' for word in words)
        for i in range(1, max_len)
    ]
    print('\n'.join(garland))
    print(' ')
    print('\n'.join(reversed(garland)))