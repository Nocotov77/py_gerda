import json


def get_req(word):
    if len(word) > 1 and word[-1].lower() in {"ь", "ы"}:
        return word[-2].lower()
    return word[-1].lower()


with open("russian_words.json", "r", encoding="utf-8") as f:
    rw = json.load(f)
valid = {}
for k, lst in rw.items():
    valid[k.lower()] = set(w.lower() for w in lst)

used = set()
turn = "user"
req = None

while True:
    if turn == "user":
        try:
            usr = input().strip()
        except EOFError:
            break
        if usr.lower() == "сдаюсь":
            print("Игра закончена! Победил компьютер.")
            break
        word = usr.lower()
        if word in used:
            print("Это слово уже было.")
            continue
        if req is not None and word[0].lower() != req:
            print(f"Это слово не на букву {req}.")
            continue
        if word[0].lower() not in valid or word not in valid[word[0].lower()]:
            print("Такого слова нет.")
            continue
        used.add(word)
        req = get_req(word)
        turn = "comp"
    else:
        if req not in valid:
            print("Игра закончена! Победил пользователь.")
            break
        opts = [w for w in valid[req] if w not in used]
        if not opts:
            print("Игра закончена! Победил пользователь.")
            break
        comp = sorted(opts)[0]
        print(comp)
        used.add(comp)
        req = get_req(comp)
        turn = "user"