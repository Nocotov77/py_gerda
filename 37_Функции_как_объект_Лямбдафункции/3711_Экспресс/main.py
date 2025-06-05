def express(*stops):
    return list(map(lambda x: x[1], filter(lambda x: 
                                           not (len(x[1]) < 8 or len(x[1]) == len(set(x[1])) 
                                                or any(ch.isdigit() and int(ch) % 2 == 0 
                                                       for ch in x[1]) or x[0] % 7 == 0), 
                                           enumerate(stops, 1))))