def average(marks):
    try:
        print(sum(marks) / len(marks))
    except ZeroDivisionError:
        print("0")
