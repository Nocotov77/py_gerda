s = float(input())
d = float(input())
reduced_speed = s * (1 - 0.02 * d)
minimal_speed = s * 0.5
result = max(reduced_speed, minimal_speed)
print(result)