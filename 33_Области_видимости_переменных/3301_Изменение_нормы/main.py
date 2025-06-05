def changing_the_norm(lst):
    if not hasattr(changing_the_norm, "prev"):
        changing_the_norm.prev = 0
    cnt = sum(1 for x in lst if x > changing_the_norm.prev)
    changing_the_norm.prev = sum(lst) / len(lst) if lst else 0
    return cnt