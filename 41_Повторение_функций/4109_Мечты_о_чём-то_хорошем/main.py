def good_dreams(text, first_divisor, second_divisor, *args, **kwargs):
    res = [row.split(second_divisor) for row in text.split(first_divisor)]
    for func_name, idx in args:
        if func_name in kwargs and 0 <= idx < len(res):
            f = kwargs[func_name]
            res[idx] = [f(item) for item in res[idx]]
    return res
