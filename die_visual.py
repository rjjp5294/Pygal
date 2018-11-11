from die import Die

# Creating a D6 (6 sided die)

die_1 = Die()

# Now creating a second die for extended testing

die_2 = Die()

# Make some rolls, and store results into the list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyzing the frequencies
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualizing the results of rolling 2 D6 at the same time
hist = pygal.Bar()

hist.title = "Result of Rolling two D6 1000 times."

x_label_values = []
for i in range(2, max_result+1):
    x_label_values.append(str(i))

hist.x_labels = x_label_values
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')