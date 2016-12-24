import datetime

start = datetime.datetime.strptime("1-1-1901", "%d-%m-%Y")
end = datetime.datetime.strptime("31-12-2000", "%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
counter = 0
for date in date_generated:
    if date.strftime("%A") == "Sunday" and date.day == 1:
        counter += 1
print(counter)