def cash_withdrawal(value):
    if value > 50000:
        return "Exceeded the limit"
    total = sum(k * atm[k] for k in atm)
    if total < value:
        return "Insufficient funds"
    remaining = value
    used = {}
    for d in sorted(atm.keys(), reverse=True):
        if remaining >= d:
            num = min(atm[d], remaining // d)
            if num:
                used[d] = num
                remaining -= num * d
    if remaining:
        return "Insufficient funds"
    for d in used:
        atm[d] -= used[d]
    return "\n".join(f"{used[d]} bills of {d} rubles each" for d in sorted(used.keys(), reverse=True))