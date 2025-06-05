def porcupine(*tuples):
    avg_first = sum(t[0] for t in tuples) / len(tuples)
    avg_second = sum(t[1] for t in tuples) / len(tuples)
    return sorted(list(filter(lambda t: t[0] > avg_first and t[1] < avg_second, tuples)))