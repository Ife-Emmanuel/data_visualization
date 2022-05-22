import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = r'C:\Users\User\PycharmProjects\data_visualization\csv_file_format\sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    index = header_row.index('TMAX')
    print('index', index)
    indexl = header_row.index('TMIN')
    indexd = header_row.index('DATE')


    dates, highs, lows = [], [], []
    hhighs, llows = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[indexd], '%Y-%m-%d')
            hhigh = row[index]
            llow = row[indexl]
            hhighs.append(hhigh)
            llows.append(llow)
            high = int(row[index])
            low = int(row[indexl])
        except ValueError:
            print(current_date, 'missing data')
            shigh = row[index]
            print('high', high)
            print('low', low)
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


    # Plot data.
    fig = plt.figure(figsize= (10, 6), dpi= 128, facecolor= (0, 0.7, 0.7))
    # plt.axis([0, 100, 0, 100])
    plt.plot(dates, highs, c= 'red', alpha= 0.5)
    plt.plot(dates, lows, c= 'blue', alpha= 0.5)
    plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha= 0.1)

    # Format plot.
    plt.title('Daily high and low temperatures - 2014', fontsize= 24)
    plt.ylabel('Temperature (F)', fontsize= 16)
    plt.xlabel('', fontsize= 16)
    plt.tick_params(axis= 'both', which = 'major', labelsize= 4)
    fig.autofmt_xdate()

    # plt.xlabel('', fontsize= 16)
    print('highs', highs)
    print('lows', lows)
    print('hhighs', hhighs)
    print('llows', llows)

    print(len(highs))
    print(len(lows))
    print('hhighs : ', len(hhighs))
    print('llows : ', len(llows))
    plt.show()
