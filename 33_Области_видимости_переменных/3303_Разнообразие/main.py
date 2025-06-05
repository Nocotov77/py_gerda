def diversity(x):
    if not hasattr(diversity, "counts"):
        diversity.counts = {}
    diversity.counts[x] = diversity.counts.get(x, 0) + 1
    return diversity.counts[x]