print(", ".join(map(lambda n: (n.split()[-1][:-3] + "lone") if n.split()[-1].lower().endswith("ino")
                    else (n.split()[-1][:-2] + "ino"), filter(lambda x: len(x.split()) > 1,
                                                              input().split("; ")))))
