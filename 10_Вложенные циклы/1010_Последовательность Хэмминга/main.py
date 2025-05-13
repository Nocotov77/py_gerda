import heapq

n = int(input())

heap = [2, 3, 5]
heapq.heapify(heap)
visited = {2, 3, 5}
result = []

while len(result) < n:
    current = heapq.heappop(heap)
    result.append(current)
    for multiplier in [2, 3, 5]:
        next_num = current * multiplier
        if next_num not in visited:
            heapq.heappush(heap, next_num)
            visited.add(next_num)

print(result[n - 1])