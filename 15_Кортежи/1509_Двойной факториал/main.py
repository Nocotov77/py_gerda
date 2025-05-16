def double_factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result

def generate_double_factorial_list(n):
    result_list = []
    for i in range(n + 1):
        result_list.append((i, double_factorial(i)))
    return result_list

n = int(input())
result = generate_double_factorial_list(n)
print(result)
