word = input().strip()
n = len(word)

if n % 2 == 1:
    m = n // 2
    for i in range(m + 1):
        left_pad = " " * (m - i)
        if i == 0:
            print(left_pad + word[m])
        else:
            inner_space = " " * (2 * i - 1)
            print(left_pad + word[m - i] + inner_space + word[m + i])
else:
    k = n // 2
    left_center = k - 1
    right_center = k
    for i in range(k):
        left_pad = " " * ((k - 1) - i)
        if i == 0:
            print(left_pad + word[left_center] + word[right_center])
        else:
            inner_space = " " * (2 * i)
            print(left_pad + word[left_center - i] + inner_space + word[right_center + i])
