def epic_hero(arr, knight):
    if not arr:
        return [knight]
    if knight <= arr[0]:
        return [knight] + arr
    return [arr[0]] + epic_hero(arr[1:], knight)