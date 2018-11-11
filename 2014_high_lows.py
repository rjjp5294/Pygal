import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f) # This passes the files and creates a reader object associated with the file
    header_row = next(reader) #This function returns the next line in the file when passed a reader object, and since we call
    # it only once we get the first line from the file. In this case this contains the files headers.
    # The reader processes the first line of the CSVs in the file and stores each as an item in a list
    #
    # print(header_row)
    #
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    #
    dates, highs, lows = [], [], [] #Can define multiple lists seperatly in the same line using this format apparently
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d") #Using strptime method to extract the date strings from the CSV
        #file from each line and indicating to Python how the date is formatted so we can work with it later
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)
    #The reader object continues from where it left off, returning each line following it's current position.
    #Since we already read the 'header' row, the loop begins at the second line of the CSV file where the actual data starts.
    #In this case, since the 'Max Temp' is at index[1] of the headers object, all associated data with max temp is at index[1]
    #of each following line of data i.e. max temp was the second column in the table and that's how it translates now.
    #We extract the index[1] item of every line and append to the highs[].

        low = int(row[3])
        lows.append(low)


#Plotting the data on pygal
line = pygal.Line(x_label_rotation=20)
line.title = '2014 Daily High vs Low Temps in Sitka, AL'
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
plt.title('2014 Daily High and Low Temps in Sitka, AL', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate() #this
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.legend(loc='upper left', fontsize=8)

plt.show()