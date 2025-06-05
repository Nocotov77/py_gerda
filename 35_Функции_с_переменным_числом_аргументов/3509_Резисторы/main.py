def circuit_resistance(*resistors, connection="serial", conductivity=False):
    if connection == "serial":
        total = sum(resistors)
        result = 1 / total if conductivity and total else total
    elif connection == "parallel":
        inv_sum = sum(1 / r for r in resistors)
        result = inv_sum if conductivity else 1 / inv_sum if inv_sum else 0
    return round(result, 4)