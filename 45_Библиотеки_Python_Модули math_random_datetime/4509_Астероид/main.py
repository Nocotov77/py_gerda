from datetime import datetime, date


def asteroid_angle(T):
    epoch = date(2000, 1, 1)
    today = datetime.today().date()
    days = (today - epoch).days
    return round(((days % T) / T) * 360)