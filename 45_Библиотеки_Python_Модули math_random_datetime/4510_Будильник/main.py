from datetime import datetime, timedelta


def alarm(date_str, delta=10):
    order_date = datetime.strptime(date_str, "%Y-%m-%d")
    start_date = datetime(2021, 1, 4)
    week_num = ((order_date.date() - start_date.date()).days // 7) + 1
    day = order_date.weekday()
    if day in (5, 6):
        base = "10:00" if week_num % 2 == 1 else "11:00"
        return (base,)
    else:
        if week_num % 2 == 1:
            base = "07:45" if day == 3 else "08:30"
        else:
            base = "09:00" if day in (0, 1, 4) else "09:30"
        h, m = map(int, base.split(":"))
        second = (datetime(2000, 1, 1, h, m) + timedelta(minutes=delta)).strftime("%H:%M")
        return (base, second)