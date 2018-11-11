import pygal
from die import Die

# Creating a D6 (6 sided die)

die_1 = Die(7)
die_1_sides = die_1.num_sides

# Now creating a second die for extended testing

die_2 = Die(10)
die_2_sides = die_2.num_sides

# Creating thrid die for even more extended testing

die_3 = Die()
die_3_sides = die_3.num_sides

# Make some rolls, and store results into the list
results = []
num_of_rolls = 10000
for roll_num in range(num_of_rolls):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyzing the frequencies
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualizing the results of rolling 2 D6 at the same time
hist = pygal.Bar()

title_of_graph = "Result of Rolling a D", str(die_1_sides), ", a D", str(die_2_sides), ", and a D", \
                 str(die_3_sides), " ", "{:,}".format(num_of_rolls), " times."
hist.title = ''.join(title_of_graph)

x_labels_values = ([str(i) for i in range(3, max_result+1)])
# for i in range(2, max_result+1):
#     x_label_values.append(str(i))

hist.x_labels = x_labels_values
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D + D + D',frequencies)
hist.render_to_file('different_die_visual.svg')