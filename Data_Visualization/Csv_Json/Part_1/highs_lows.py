import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtém as temperaturas máximas do arquivo
file_name = 'Csv_Json\Part_1\sitka_weather_2014.csv'

with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])  

        except ValueError:
            print(current_date, 'missing data') 
        
        else:

            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Faz a plotagem dos dados
fig = plt.figure(dpi=120, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Formata o gráfico
plt.title("Daily high and low temperatures - 2014", fontsize=14)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
