from datetime import datetime


def days_left(date_str):
    target = datetime.strptime(date_str, "%d.%m.%Y").date()
    today = datetime.today().date()
    return (target - today).days