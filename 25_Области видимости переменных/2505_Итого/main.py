def total(data):
    if not hasattr(total, "dishes"):
        total.dishes = {}
    for line in data:
        dish, cal = line.rsplit(maxsplit=1)
        cal = float(cal)
        if dish in total.dishes:
            cnt, tot_cal = total.dishes[dish]
            total.dishes[dish] = (cnt + 1, tot_cal + cal)
        else:
            total.dishes[dish] = (1, cal)
    overall = 0
    lines_out = []
    for dish in sorted(total.dishes):
        cnt, tot_cal = total.dishes[dish]
        overall += tot_cal
        lines_out.append(f"{dish} - {cnt} - {tot_cal:.1f} kCal")
    lines_out.append("------")
    lines_out.append(f"Total: {overall:.1f} kCal")
    print("\n".join(lines_out))
    print()

data = ["Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)
data = ["Orange juice drink 54.5",
        "Ice cream, strawberry 192",
        "Puff pastry with protein cream 461"]
total(data)
