def permission(code):
    attempt = input()
    if sum(int(digit) for digit in code) == sum(int(digit) for digit in attempt):
        print("ACCESS IS ALLOWED")
    else:
        print("ACCESS IS DENIED")