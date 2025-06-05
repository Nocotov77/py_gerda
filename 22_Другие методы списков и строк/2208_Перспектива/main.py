heights = list(map(int, input().split()))
visible = []
max_height = 0

for h in heights:
    if h > max_height:
        visible.append(str(h))
        max_height = h

print('>>'.join(visible))