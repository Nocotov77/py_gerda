def dict_flip(*args):
    result = {}
    for i in range(0, len(args), 2):
        if i + 1 < len(args):
            try:
                key = args[i + 1].decode('utf-8')
                value = args[i].decode('utf-8')
                if not key.startswith("b'"):
                    result[key] = value
            except (UnicodeDecodeError, AttributeError):
                continue
    return result if result else None