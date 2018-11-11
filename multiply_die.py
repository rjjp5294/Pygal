import pygal
from die import Die

die_1 = Die()
die_2= Die()

results = []
num_of_rolls = 10000
for roll_num in range(num_of_rolls):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualizing the results of rolling 2 D6 at the same time
hist = pygal.Bar()

title_of_graph = "Result of Rolling a D", str(die_1.num_sides), " and a D", \
                 str(die_2.num_sides), " ", "{:,}".format(num_of_rolls), " times."
hist.title = ''.join(title_of_graph)

x_labels_values = ([str(i) for i in range(1, max_result+1)])

hist.x_labels = x_labels_values
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D + D',frequencies)
hist.render_to_file('multiply_die_visual.svg')