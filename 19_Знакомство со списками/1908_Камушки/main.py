n = int(input())
stones = [int(input()) for _ in range(n)]
total_sum = sum(stones)
sum_parity = total_sum % 2

remaining = []
removed_sum = 0

for num in stones:
    if num % 2 == sum_parity:
        remaining.append(num)
    else:
        removed_sum += num

print(f"{removed_sum} {remaining}")