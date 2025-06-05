def get_expensive(item):
    if not hasattr(get_expensive, "prev"):
        get_expensive.prev = []
    if "gnome" not in item.lower():
        return "What do you offer for freedom, gnome?"
    get_expensive.prev.append(item)
    return max(get_expensive.prev, key=lambda item: (len(item)))