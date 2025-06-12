def diff_by_one(a, b):
    if len(a) != len(b):
        return False
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1


words = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line.strip() == "":
        continue
    words.append(line.strip())
first_word = words[0]
last_word = words[-1]
intermediate = words[1:-1]


def dfs(chain, used):
    if len(chain) == len(intermediate) + 1:
        if diff_by_one(chain[-1], last_word):
            return chain
        return None
    for i in range(len(intermediate)):
        if not used[i] and diff_by_one(chain[-1], intermediate[i]):
            used[i] = True
            res = dfs(chain + [intermediate[i]], used)
            if res is not None:
                return res
            used[i] = False
    return None


used = [False] * len(intermediate)
sol = dfs([first_word], used)
if sol is not None:
    sol.append(last_word)
    for w in sol:
        print(w)