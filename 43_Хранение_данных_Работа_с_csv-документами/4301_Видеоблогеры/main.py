import csv

year = input().strip()
top_channels = []
total_subscribers = 0
categories = set()

with open("top_youtube_channels_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["started"] == year:
            if len(top_channels) < 3:
                top_channels.append(row["youtuber"])
                total_subscribers += int(row["subscribers"].replace(",", ""))
            categories.update(row["category"].split("; "))

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(", ".join(top_channels) + "\n")
    f.write(str(total_subscribers) + "\n")
    f.write("; ".join(sorted(categories)) + "\n")