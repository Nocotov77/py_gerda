import csv
import json


def check_security(name, place):
    with open("taxpayer_in.json", "r", encoding="utf-8") as f:
        taxpayers = json.load(f)
    client = None
    for t in taxpayers:
        if t["lastname"] == name[0] and t["firstname"] == name[1] and t["middlename"] == name[2]:
            client = t
            break
    if client is None:
        return (None, None)
    tin = client.get("tin", "")
    if len(tin) != 12 or not tin.isdigit():
        cs = -1
    else:
        coefs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        s1 = sum(int(tin[i]) * coefs1[i] for i in range(10))
        r1 = s1 % 11
        digit1 = r1 % 10
        coefs2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
        s2 = sum(int(tin[i]) * coefs2[i] for i in range(11))
        r2 = s2 % 11
        digit2 = r2 % 10
        cs = 0 if (digit1 == int(tin[10]) and digit2 == int(tin[11])) else -1
    regions = {}
    with open("regions.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            regions[row[1]] = row[0]
    region_code = regions.get(place)
    rc = 0 if region_code is not None and tin[:2] == region_code else -1
    return (rc, cs)


if __name__ == "__main__":
    pass