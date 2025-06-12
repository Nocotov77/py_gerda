import random


def generate_fandom(n, names):
    chosen_names = random.sample(names, n)
    distances = random.sample(range(100, 501), n)
    cities = []
    for i in range(n):
        size = random.randint(10, 20)
        population = random.randint(1, 100) * 10000
        cities.append((chosen_names[i], size, population, distances[i]))
    return cities