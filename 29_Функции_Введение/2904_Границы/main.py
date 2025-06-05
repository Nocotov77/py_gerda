def borders(tl, br, pt):
    x1, y1 = tl
    x2, y2 = br
    x, y = pt
    if x1 < x < x2 and y2 < y < y1:
        print("INSIDE")
    elif x1 <= x <= x2 and y2 <= y <= y1:
        print("AT THE EDGE")
    else:
        print("OUTSIDE")