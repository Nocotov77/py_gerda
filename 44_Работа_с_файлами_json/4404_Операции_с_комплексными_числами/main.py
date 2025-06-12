import json

with open("in.json", "r", encoding="utf-8") as f:
    data = json.load(f)
z1 = data["complex"][0]
z2 = data["complex"][1]
sum_res = {"Re": z1["Re"] + z2["Re"], "Im": z1["Im"] + z2["Im"]}
diff_res = {"Re": z1["Re"] - z2["Re"], "Im": z1["Im"] - z2["Im"]}
prod_res = {"Re": z1["Re"] * z2["Re"] - z1["Im"] * z2["Im"], "Im": z1["Re"] * z2["Im"] + z1["Im"] * z2["Re"]}
result = {"complex": [sum_res, diff_res, prod_res]}
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)