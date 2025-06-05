s = input().strip()
left = 0
right = len(s) - 1
is_palindrome = True

while left <= right:
    while left <= right and s[left] == ' ':
        left += 1
    while left <= right and s[right] == ' ':
        right -= 1
    if left > right:
        break
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)