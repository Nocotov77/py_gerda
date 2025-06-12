import math
from datetime import datetime, timedelta


cost = float(input().strip())
disc = float(input().strip())
days = int(input().strip())
order_date = datetime.strptime(input().strip(), "%d.%m.%Y")
order_time = input().strip()
h, m = map(int, order_time.split(':'))
total_minutes = h * 60 + m
if 360 <= total_minutes <= 750:
    new_cost = math.floor(cost * (100 - disc) / 100)
    if order_date.weekday() != 0:
        days = max(days - 1, 0)
else:
    new_cost = math.floor(cost)
delivery_date = order_date + timedelta(days=days)
print(delivery_date.strftime("%d-%m-%Y"), new_cost)