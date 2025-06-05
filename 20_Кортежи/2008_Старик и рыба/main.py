unique_fish = []
seen = set()


while True:
    line = input().strip()
    if not line:
        break
    if line not in seen:
        seen.add(line)
        unique_fish.append(line)


def bubble_sort_alpha(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


sorted_alpha = bubble_sort_alpha(unique_fish.copy())
sorted_length = bubble_sort_length(unique_fish.copy())

if sorted_alpha == sorted_length:
    print("YES")
else:
    for i in range(len(sorted_alpha)):
        if sorted_alpha[i] != sorted_length[i]:
            print(f"{sorted_alpha[i]} {sorted_length[i]}")
            break