def anthropic_principle(*nums, k=2):
    lo = min(nums)
    hi = max(nums)
    nums_set = set(nums)
    res = []
    for n in range(lo + 1, hi):
        if n in nums_set:
            continue
        divs = []
        r = int(n ** 0.5)
        for d in range(2, r + 1):
            if n % d == 0:
                divs.append(d)
                if d != n // d:
                    divs.append(n // d)
        divs = sorted(divs)
        if len(divs) == k:
            res.append(tuple(divs))

    def prod(t):
        p = 1
        for x in t:
            p *= x
        return p
    return sorted(res, key=prod)