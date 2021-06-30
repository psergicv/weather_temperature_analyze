from matplotlib import pyplot as plt
from datetime import datetime
import csv

filename = 'berlin_may_2020_temps.csv'

with open(filename) as file:
    reader = csv.reader(file)
    headers_row = next(reader)

    dates, high_temps, low_temps = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            max_temp = float(row[3])
            min_temp = float(row[2])
        except ValueError:
            print(current_date, 'The data is missing')
        else:
            dates.append(current_date)
            high_temps.append(max_temp)
            low_temps.append(min_temp)


fig = plt.figure(dpi=128, figsize=(20, 6))
plt.plot(dates, high_temps, c='red', alpha=0.5)
plt.plot(dates, low_temps, c='blue', alpha=0.5)
plt.fill_between(dates, high_temps, low_temps, facecolor='green', alpha=0.1)
plt.title("Daily high & low temperatures - May, 2020", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (Celsius)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
