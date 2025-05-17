def diversity(x):
    if not hasattr(diversity, "counts"):
        diversity.counts = {}
    diversity.counts[x] = diversity.counts.get(x, 0) + 1
    return diversity.counts[x]

print(diversity("Happy"))
print(diversity("New"))
print(diversity("Year"))
print(diversity("Year"))
print(diversity("Year"))
