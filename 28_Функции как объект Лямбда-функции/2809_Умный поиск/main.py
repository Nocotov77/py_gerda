def smart_search(*args, func):
    if all(isinstance(x, int) for x in args):
        return tuple(filter(func, args))
    elif all(isinstance(x, str) for x in args):
        return tuple(filter(lambda s: s and s[0].isupper(), args))
