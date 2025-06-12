from datetime import datetime, timedelta


capacity = float(input().strip())
charge_duration = int(input().strip())
speed = float(input().strip())
departure_str = input().strip()
departure = datetime.strptime(departure_str, "%d.%m.%Y %H:%M")
stations = list(map(int, input().split()))
last_charge = 0
current_time = departure
stops = []
for i in range(len(stations)):
    dist = stations[i]
    travel = dist - last_charge
    tmin = round((travel / speed) * 60)
    arrival = current_time + timedelta(minutes=tmin)
    if i < len(stations) - 1:
        next_seg = stations[i + 1] - dist
        rem = capacity - travel
        if rem < next_seg:
            stops.append((i + 1, arrival))
            last_charge = dist
            current_time = arrival + timedelta(minutes=charge_duration)
for num, t in stops:
    print(num, t.strftime("%d-%m-%Y %H:%M"))