import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) # This passes the files and creates a reader object associated with the file
    header_row = next(reader) #This function returns the next line in the file when passed a reader object, and since we call

    dates, highs, lows = [], [], []
    for row in reader:
        try: #Program will run through file and check if data is there for each date
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])

        except ValueError:#if any data is missing, error message for that date will print and program will continue to next date
            print(current_date, 'Missing Data')
        else:#if no error occurs, we append the corresponding data to the lists for plotting
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


#Plotting the data on pygal
line = pygal.Line(x_label_rotation=20)
line.title = '2014 Daily High vs Low Temps in Death Valley, CA'
line.x_labels = dates
line.x_title= 'Date'
line.y_title= 'Temperature (F)'

line.add('Highs', highs)
line.add('Lows', lows)

#line.render_to_file('2014_high_lows_visual.svg')

#Plotting the data on matplotlib
fig = plt.figure(dpi=135, figsize=(10, 6))
plt.plot(dates, highs, c='red', label='Highs', alpha=0.85)
plt.plot(dates, lows, c='blue', label='Lows', alpha=0.85)
plt.fill_between(dates, highs, lows, facecolor='blue',
                 alpha=0.35)

# Formatting the plot
plt.title('2014 Daily High and Low Temps in Death Valley', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate() #this
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.legend(loc='upper left', fontsize=8)

plt.show()