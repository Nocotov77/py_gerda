def haystack(*args, needle):
    if not args:
        return -1
    if args[0] == needle:
        return 0
    sub = haystack(*args[1:], needle=needle)
    return sub + 1 if sub != -1 else -1