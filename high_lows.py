import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
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
    dates, highs = [], [] #Can define 2 lists seperatly in the same line using this format apparently
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




#Plotting the data (matplotlib)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Formatting the plot
plt.title('July 2014 Daily High Temps in Sitka, AL', fontsize=16)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate() #this
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()