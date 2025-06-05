def line(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    k_val = round(k, 2)
    b_val = round(b, 2)
    if abs(k_val) < 1e-9:
        k_val = 0.0
    sign = " - " if b_val < 0 else " + "
    print(f"y = {k_val} * x{sign}{abs(b_val)}")