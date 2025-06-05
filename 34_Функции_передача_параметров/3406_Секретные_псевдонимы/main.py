def secret_sort():
    secret_avatars.sort(key=lambda s: sum(1 for i in range(1, len(s), 2) if s[i] in "aeiouyAEIOUY"))