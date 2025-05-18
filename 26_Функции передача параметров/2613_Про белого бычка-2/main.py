def print_cow():
    class Marker:
        def __repr__(self):
            return '[...]'

    marker = Marker()

    def expand(obj, depth):
        if not isinstance(obj, list):
            return obj
        new_list = []
        for item in obj:
            if item is cow:
                if depth:
                    new_list.append(expand(cow, depth - 1))
                else:
                    new_list.append(marker)
            else:
                new_list.append(item)
        return new_list

    print(expand(cow, 2))