n = int(input())
data = []
for _ in range(n):
    height = int(input())
    iron = float(input())
    data.append((height, iron))


def find_max_index(arr, start):
    max_index = start
    for i in range(start + 1, len(arr)):
        current = arr[i]
        max_elem = arr[max_index]
        if current[0] > max_elem[0]:
            max_index = i
        elif current[0] == max_elem[0]:
            if current[1] > max_elem[1]:
                max_index = i
    return max_index


for i in range(len(data)):
    max_i = find_max_index(data, i)
    data[i], data[max_i] = data[max_i], data[i]

for item in data:
    print(f"({item[0]}, {item[1]})")