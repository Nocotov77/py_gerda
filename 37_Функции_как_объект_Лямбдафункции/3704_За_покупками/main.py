print("\n".join(map(lambda x: x[1:] if x.startswith("*") else x, 
                    filter(lambda x: x.startswith("*") or x[0].upper() != "V", input().split("; ")))))