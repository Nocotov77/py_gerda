def best_future(*args):
    n = len(args)
    res = [-1] * n
    stack = []
    for i, x in enumerate(args):
        while stack and args[stack[-1]] > x:
            res[stack.pop()] = i
        stack.append(i)
    return res

