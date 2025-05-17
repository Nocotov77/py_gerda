def changing_the_norm(lst):
    if not hasattr(changing_the_norm, "prev"):
        changing_the_norm.prev = 0
    cnt = sum(1 for x in lst if x > changing_the_norm.prev)
    changing_the_norm.prev = sum(lst) / len(lst) if lst else 0
    return cnt

print(changing_the_norm([150, 160, 164, 147]))
print(changing_the_norm([170, 162, 156, 153, 159]))
print(changing_the_norm([158, 168, 172]))