def catch_flies(*flies, func=None):
    filtered = [fly for fly in flies if func is None or func(fly['x'], fly['y'])]
    min_x = min(fly['x'] for fly in filtered)
    max_x = max(fly['x'] for fly in filtered)
    min_y = min(fly['y'] for fly in filtered)
    max_y = max(fly['y'] for fly in filtered)
    return ({"x": min_x, "y": max_y}, {"x": max_x, "y": min_y})