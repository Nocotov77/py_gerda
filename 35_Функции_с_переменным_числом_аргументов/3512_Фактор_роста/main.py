def nutrient_medium(portions, *factors, periods=1, mult=1):
    dishes = len(factors)
    base = portions // dishes
    rem = portions % dishes
    distribution = [base + (1 if i < rem else 0) for i in range(dishes)]
    results = []
    for i in range(dishes):
        amt = distribution[i]
        for _ in range(periods):
            amt = amt * factors[i] * mult
            if amt < 0:
                amt = 0
        results.append(round(amt, 3))
    total = round(sum(results), 3)
    return total, results